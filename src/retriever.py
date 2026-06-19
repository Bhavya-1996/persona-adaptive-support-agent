from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


class SupportRetriever:

    def __init__(self):

        self.embedding_model = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        self.persist_directory = "chroma_db"

        self.vector_db = None

    def load_documents(self):

        loader = DirectoryLoader(
            "data",
            glob="**/*.*"
        )

        documents = loader.load()

        return documents

    def split_documents(self, documents):

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100
        )

        chunks = splitter.split_documents(
            documents
        )

        return chunks

    def create_vector_store(self):

        documents = self.load_documents()

        chunks = self.split_documents(
            documents
        )

        self.vector_db = Chroma.from_documents(
            documents=chunks,
            embedding=self.embedding_model,
            persist_directory=self.persist_directory
        )

        return self.vector_db

    def load_vector_store(self):

        self.vector_db = Chroma(
            persist_directory=self.persist_directory,
            embedding_function=self.embedding_model
        )

        return self.vector_db

    def retrieve(self, query, k=3):

        if self.vector_db is None:
            self.load_vector_store()

        results = self.vector_db.similarity_search(
            query,
            k=k
        )

        return results
