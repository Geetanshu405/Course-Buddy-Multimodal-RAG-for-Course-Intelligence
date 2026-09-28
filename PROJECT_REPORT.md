# AI-Powered RAG-Based Course Recommendation System

## Project Report

### Project Title

**AI-Powered Retrieval-Augmented Generation (RAG) Based Course Recommendation System**

### Author

**Geetanshu Bhavsar**

### Institution

**Sandip University**

### Submission Date

**May 2026**

---

# Abstract

This project presents the development of an AI-powered Retrieval-Augmented Generation (RAG) based course recommendation system capable of retrieving and generating contextual recommendations from multiple educational datasets.

The system was designed to intelligently answer user queries regarding online courses from platforms such as **Coursera, Udemy, and Udacity**.

The primary objective of the project was to create a conversational AI assistant capable of retrieving highly relevant educational content while minimizing hallucinations commonly associated with Large Language Models (LLMs).

The system integrates:

- NVIDIA embedding models
- ChromaDB vector storage
- LangChain orchestration
- NVIDIA-hosted Large Language Models

These components work together to deliver grounded and structured responses.

Throughout the development lifecycle, several technical challenges were encountered, including:

- Retrieval inaccuracies
- Metadata propagation failures
- Hallucinated responses
- Stale vector database issues
- Prompt engineering problems
- Conversational memory limitations

These issues were systematically debugged and resolved through iterative testing and architectural improvements.

## Key Achievements

Key achievements of the project include:

- Development of a modular RAG architecture
- Metadata-aware retrieval with URL grounding
- Conversational history-aware query reformulation
- Dynamic retrieval optimization using MMR search
- Platform-specific filtering
- Structured AI-generated responses
- Hallucination prevention mechanisms
- Persistent vector database integration

The final system demonstrates strong contextual retrieval performance and conversational AI capabilities while remaining scalable and extensible for future deployment as a web-based educational assistant.

---

# 1. Introduction

## 1.1 Background

The rapid growth of online learning platforms has created an overwhelming amount of educational content available to learners.

Platforms such as **Coursera, Udemy, and Udacity** offer thousands of courses across domains including:

- Artificial Intelligence
- Machine Learning
- Web Development
- Data Science
- Cloud Computing

Although these platforms provide search functionality, users often struggle to find the most suitable courses based on:

- Difficulty level
- Prerequisites
- Ratings
- Duration
- Platform preference
- Learning goals

Traditional keyword-based search systems frequently fail to understand conversational or context-aware user queries.

Recent advancements in Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG) systems provide an opportunity to improve educational recommendation systems by combining semantic search with contextual AI-generated responses.

---

## 1.2 Problem Statement

Traditional course search systems suffer from several limitations:

- Lack of conversational understanding
- Poor contextual retrieval
- Inability to remember previous queries
- Hallucinated AI responses
- Limited personalization
- Weak metadata utilization
- Poor handling of multi-platform datasets

The goal of this project was to design and implement a robust RAG-based conversational assistant capable of retrieving highly relevant educational courses from structured datasets while generating grounded and accurate responses.

---

# 1.3 Objectives

The primary objectives of the project were:

1. Build a modular Retrieval-Augmented Generation pipeline.
2. Create a vector database using educational datasets.
3. Generate semantic embeddings for course data.
4. Implement conversational memory and history-aware retrieval.
5. Support platform-specific filtering.
6. Retrieve metadata such as URLs, ratings, and durations.
7. Prevent hallucinated AI responses.
8. Improve retrieval precision using optimization strategies.
9. Develop a scalable architecture for future deployment.

---

# 1.4 Motivation

The motivation behind this project originated from the growing importance of AI-powered educational tools and the practical relevance of Retrieval-Augmented Generation systems in modern AI applications.

The project also served as a hands-on learning experience for understanding:

- Vector databases
- Semantic search
- Embedding models
- Prompt engineering
- Conversational AI systems
- Modular software architecture
- AI debugging and optimization workflows

The development process provided practical exposure to real-world AI engineering challenges beyond theoretical learning.

---

# 2. Technology Stack

## 2.1 Programming Language

| Technology | Purpose |
|---|---|
| Python | Core backend development and AI orchestration |

Python was selected due to its extensive ecosystem for AI, machine learning, and vector database integration.

---

## 2.2 AI and RAG Frameworks

| Framework | Purpose |
|---|---|
| LangChain | RAG orchestration and LLM integration |
| ChromaDB | Vector database storage and retrieval |
| NVIDIA AI Endpoints | Embedding and LLM inference |

### LangChain

LangChain was selected for its modular support for:

- Retrieval pipelines
- Memory management
- Prompt engineering
- Conversational chains

### ChromaDB

ChromaDB was selected because it provides lightweight local vector storage with strong integration support for LangChain.

### NVIDIA AI Endpoints

NVIDIA AI Endpoints were selected because they provide production-quality embedding models and large language models accessible through APIs.

---

## 2.3 Embedding Model

| Model | Purpose |
|---|---|
| `nvidia/nv-embed-v1` | Semantic embedding generation |

The NVIDIA embedding model was used to convert course information into dense vector representations suitable for semantic retrieval.

---

## 2.4 Large Language Model

| Model | Purpose |
|---|---|
| `meta/llama-3.1-70b-instruct` | Response generation |

The LLM was responsible for:

- Query reformulation
- Context-aware answer generation
- Conversational response generation
- Structured output formatting

---

## 2.5 Additional Libraries

| Library | Purpose |
|---|---|
| pandas | CSV dataset processing |
| dotenv | Environment variable management |
| os | File handling |
| Black Formatter | Code formatting |

---

# 3. System Architecture

## 3.1 Overall Workflow

The complete system architecture follows a modular Retrieval-Augmented Generation pipeline.

### Workflow Steps

1. Load CSV datasets.
2. Process and structure course information.
3. Generate embeddings using NVIDIA embedding model.
4. Store embeddings in ChromaDB.
5. Accept user query.
6. Reformulate conversational query.
7. Retrieve relevant documents using vector similarity.
8. Construct contextual prompt.
9. Generate grounded response using LLM.
10. Maintain conversation history.

---

# 3.2 RAG Pipeline Architecture

The project architecture was divided into four primary modules:

| File | Responsibility |
|---|---|
| `1_ingestion_pipeline.py` | Data loading and vector database creation |
| `2_retrieval_pipeline.py` | Semantic retrieval testing |
| `3_answer_generation.py` | Grounded answer generation |
| `4_history_aware_generation.py` | Conversational memory and history-aware retrieval |

This modular architecture improved maintainability, debugging, and scalability.

---

# 3.3 Query Processing Flow

The user query processing flow includes four major steps.

## Step 1: Query Reformulation

Conversational follow-up queries are reformulated into standalone semantic search queries.

### Example

**User Query:**

> "Which beginner-friendly ones from Coursera?"

**Reformulated Query:**

> "Beginner-friendly machine learning courses on Coursera"

---

## Step 2: Retrieval

The retriever performs semantic search using:

- MMR (Maximum Marginal Relevance)
- Metadata filtering
- Dynamic retrieval depth

---

## Step 3: Context Construction

Retrieved documents are converted into structured contextual blocks including:

- Course name
- Platform
- Difficulty
- Rating
- URL
- Description

---

## Step 4: Response Generation

The final prompt is sent to the LLM with strict grounding instructions.

The LLM generates structured recommendations based solely on retrieved context.

---

# 4. Source Code Explanation

## 4.1 File 1 – Ingestion Pipeline

### File Name

`1_ingestion_pipeline.py`

### Purpose

This file is responsible for:

- Loading datasets
- Structuring textual content
- Generating embeddings
- Creating vector database entries
- Injecting metadata into documents

---

## Core Functionalities

### Dataset Loading

The pipeline loads CSV files from:

- Coursera dataset
- Udemy dataset
- Udacity dataset

using pandas.

---

### Metadata Injection

Metadata fields added include:

- `course_name`
- `difficulty`
- `rating`
- `platform`
- `url`

This metadata later became critical for grounded retrieval.

---

# Embedding Generation

The NVIDIA embedding model:

```text
nvidia/nv-embed-v1