
import argparse
from src.ingest import load_and_split_pdf
from src.vectorstore import build_vectorstore , load_vectorstore
from src.query import query_documents


def main():
    parser = argparse.ArgumentParser(description="Agent PDF Research Assistant")
    subparsers = parser.add_subparsers(dest="command", help="Available commands", required=True)

    ingest_parser = subparsers.add_parser("ingest" , help ="Index one or more PDFs")
    ingest_parser.add_argument ("--pdf", required=True , nargs="+" , help="Path(s) to PDF file(s)")

    query_parser = subparsers.add_parser("query", help="ask a question about indexed PDFs")
    query_parser.add_argument("--question", required=True, help="your question")

    args = parser.parse_args()

    if args.command == "ingest" :
        all_chunks = []
        for pdf_path in args.pdf:
            chunks = load_and_split_pdf(pdf_path)
            all_chunks.extend(chunks)
        build_vectorstore(all_chunks)
        print(f"Indexed {len(all_chunks)} chunks from {len(args.pdf)} file(s)")

    elif args.command == "query":
        vectorstore = load_vectorstore()
        answer = query_documents(vectorstore,args.question)
        print(answer)

if __name__ == "__main__":
    main()
