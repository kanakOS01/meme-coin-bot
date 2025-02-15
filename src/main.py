from typing import List
from pydantic import BaseModel

SPAM_COUNT = 1

class Tweet(BaseModel):
    content: str
    id: str

def get_tweets(user_id: str) -> List[Tweet]:
    pass

def get_token_from_llm():
    pass

def create_swap_inst():
    pass

def send_txn():
    pass

def main(user_id: str):
    new_tweets = get_tweets(user_id)

    for tweet in new_tweets:
        token_addr = get_token_from_llm(tweet.content)
        if token_addr:
            txn = create_swap_inst()
            for i in range(SPAM_COUNT):
                send_txn(txn)