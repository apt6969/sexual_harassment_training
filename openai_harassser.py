import os

os.environ["OPENAI_API_KEY"] = "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"


from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader("training/").load_data()
index = VectorStoreIndex.from_documents(documents)
# index.storage_context.persist()
# # rebuild storage context
# storage_context = StorageContext.from_defaults(persist_dir="./storage")
# # load index
# index = load_index_from_storage(storage_context)
query_engine = index.as_query_engine()
your_input = input("Your prompt! ")
response = query_engine.query(your_input)
#print(response.__str__)
print(response)

index.storage_context.persist()