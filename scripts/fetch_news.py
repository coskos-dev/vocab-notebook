"""
매일 비즈니스 뉴스 RSS를 가져와서 data/articles.json에 쌓는 스크립트.
GitHub Actions가 이 스크립트를 매일 자동으로 실행합니다.

이 단계에서는 AI를 사용하지 않고, 기사 원문(제목/요약/링크)만 수집합니다.
나중에 Claude API를 연결하면 여기서 표현을 자동으로 뽑아낼 수 있습니다.
"""

import json
import os
from datetime import datetime, timezone

import feedparser

# 수집할 RSS 피드 목록. 필요하면 여기에 자유롭게 추가/삭제하세요.
FEEDS = [
    {"name": "BBC Business", "url": "https://feeds.bbci.co.uk/news/business/rss.xml"},
    {"name": "NPR Economy", "url": "https://feeds.npr.org/1017/rss.xml"},
]

# 하나의 피드에서 가져올 최대 기사 수
MAX_PER_FEED = 8

# articles.json에 보관할 최대 기사 수 (오래된 것부터 삭제됨)
MAX_TOTAL_ARTICLES = 300

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "articles.json")


def load_existing():
    if not os.path.exists(DATA_PATH):
        return []
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def make_id(entry):
    # 기사 링크를 고유 ID로 사용 (중복 방지)
    return entry.get("link", entry.get("id", entry.get("title", "")))


def fetch_all():
    collected = []
    for feed in FEEDS:
        parsed = feedparser.parse(feed["url"])
        for entry in parsed.entries[:MAX_PER_FEED]:
            published = entry.get("published", "")
            collected.append(
                {
                    "id": make_id(entry),
                    "source": feed["name"],
                    "title": entry.get("title", "(제목 없음)"),
                    "summary": entry.get("summary", "")[:500],
                    "link": entry.get("link", ""),
                    "published": published,
                    "collected_at": datetime.now(timezone.utc).isoformat(),
                }
            )
    return collected


def merge(existing, new_items):
    seen_ids = {item["id"] for item in existing if item.get("id")}
    merged = list(existing)
    added = 0
    for item in new_items:
        if item["id"] and item["id"] not in seen_ids:
            merged.append(item)
            seen_ids.add(item["id"])
            added += 1

    # 최신순 정렬 (collected_at 기준), 너무 많이 쌓이면 오래된 것부터 자르기
    merged.sort(key=lambda x: x.get("collected_at", ""), reverse=True)
    merged = merged[:MAX_TOTAL_ARTICLES]
    return merged, added


def main():
    existing = load_existing()
    # 샘플 데이터는 실제 데이터가 들어오면 제거
    existing = [item for item in existing if not item.get("id", "").startswith("sample-")]

    new_items = fetch_all()
    merged, added = merge(existing, new_items)

    os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(merged, f, ensure_ascii=False, indent=2)

    print(f"새로 추가된 기사: {added}개 / 전체 저장된 기사: {len(merged)}개")


if __name__ == "__main__":
    main()
