#!/usr/bin/env python3
""" Write a Python script that provides some stats about Ngin
logs stored in MongoDB:

Database: logs
Collection: nginx
Display (same as the example):
first line: x logs where x is the number of documents
in this collection
second line: Methods:
5 lines with the number of documents with
the method = ["GET", "POST", "PUT", "PATCH", "DELETE"
in this order (see example below - warning:
it’s a tabulation before each line)
one line with the number of documents with:
method=GET
path=/status
"""
import pymongo


def logs():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = client.logs.nginx
    print(f"{mydb.count_documents({})} logs")
    print("Methods:")
    print(f"\tmethod GET: {mydb.count_documents({"method": "GET"})}")
    print(f"\tmethod POST: {mydb.count_documents({"method": "POST"})}")
    print(f"\tmethod PUT: {mydb.count_documents({"method": "PUT"})}")
    print(f"\tmethod PATCH: {mydb.count_documents({"method": "PATCH"})}")
    print(f"\tmethod DELETE: {mydb.count_documents({"method": "DELETE"})}")
    print(f"{mydb.count_documents({"path": "/status"})} status check")


if __name__ == "__main__":
    logs()
