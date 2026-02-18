# AI Data Lineage Insights

AI-powered SQL lineage and semantic metadata extraction engine.

## 🚀 Overview

`ai-data-lineage-insights` is a lightweight AI-assisted data lineage engine designed for modern data platforms.

It:
- Parses SQL queries to extract table-level and column-level lineage
- Uses LLMs to generate semantic table descriptions
- Builds a graph-based lineage model
- Exposes REST APIs for integration with data catalogs
- Demonstrates production-oriented architecture (Docker-ready)

This project reflects real-world use cases in:
- Data Catalog & Discovery
- Data Lineage & Governance
- AI-assisted metadata enrichment
- Enterprise data platforms

---

## 🏗 Architecture

Client
   ↓
FastAPI Service
   ↓
SQL Parser → Lineage Extractor
   ↓
LLM Metadata Generator
   ↓
Graph Builder (NetworkX)
   ↓
JSON Response / Graph Output

---

## 🧠 Key Features

- SQL parsing using `sqlparse`
- Table & column extraction
- AI-generated table descriptions
- Graph-based lineage modeling
- RESTful API interface
- Modular architecture

---

## 📦 Tech Stack

- Python 3.10+
- FastAPI
- sqlparse
- NetworkX
- OpenAI API (or local LLM)
- Docker-ready

---

## 📂 Project Structure



## Slack Integration Module

The system now supports Slack ingestion via:

1. Slack workspace export (JSON)
2. Live Slack API (Bot token required)

This enables extracting SQL queries from collaborative discussions to automatically derive lineage intelligence.

Architecture Extension:

Slack → Ingestion Service → SQL Extractor → Lineage Graph → AI Metadata Enrichment

