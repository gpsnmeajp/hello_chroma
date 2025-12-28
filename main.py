from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union
from sentence_transformers import SentenceTransformer
import chromadb
chroma_client = chromadb.Client()

print("ChromaDBを準備しています")

model_name = "cl-nagoya/ruri-large"
collection = chroma_client.get_or_create_collection(
    name="my_collection",
    embedding_function=chromadb.utils.embedding_functions.SentenceTransformerEmbeddingFunction(model_name=model_name)
    )

print("テキストファイルを読み込み、ドキュメントを追加しています")

# テキストファイルを改行区切りで読み込み、ドキュメントとして追加する例
with open("text.txt", "r", encoding="utf-8") as file:
    documents = [line.strip() for line in file if line.strip()]
    document_ids = [f"doc_{i}" for i in range(len(documents))]
    collection.add(documents=documents, ids=document_ids)

print("準備完了")
# 標準入力からクエリを受け取り、類似ドキュメントを検索するループ
while True:
    query = input("クエリを入力してください（終了するには 'exit' と入力）: ")
    if query.lower() == 'exit':
        break
    results = collection.query(query_texts=[query], n_results=15)
    print("上位15件の類似ドキュメント:")
    for doc in results['documents'][0]:
        print(f"- {doc}")


