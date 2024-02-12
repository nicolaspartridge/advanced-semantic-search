# Advanced Semantic Search for Real Estate Listings

## Project Overview

This project involves the development of an advanced semantic search system tailored for real estate listings. Leveraging the latest updates in Elasticsearch and integrating the new JSON mode of ChatGPT, I aim to significantly enhance search accuracy and relevance.

## Key Features

- **Enhanced Semantic Understanding**: The system comprehends complex queries, ensuring that search results strictly align with specified criteria.
- **Real Estate Focused**: Tailored to real estate listings, accommodating specific requirements like address, bedrooms, bathrooms, size, type, neighborhood, description, price, and pet-friendliness.
- **Price-Sensitive Filtering**: Capable of understanding and enforcing price constraints (e.g., properties under $200,000 or 200k etc...).

## Problem Statement

Traditional semantic searches often yield results that only partially match the user's intent. For instance, a search for "Pet-friendly townhouse downtown under 200k" might return Houses instead of townhouses, properties that allow only cats while you own a dog, or options outside the desired price range. Our system addresses these issues, focusing on real estate, to provide highly accurate and relevant listings based on the user's precise needs.

## Solution Approach

I will employ Elasticsearch's advanced capabilities, combined with the language understanding of OpenAIs API, to create a search system that:

1. **Understands Complex Queries**: Using vector embeddings and KNN search I was able to interpret and search a database of listing with detailed user requests, such as "3-bedroom townhouses in downtown Austin under $500k."
2. **Refines Search Results**: Utilizing LLMs text to JSON to build filter queries I was able to eliminate irrelevant listings, ensuring that all results meet the specified criteria.

## Expected Outcomes

The project aims to deliver a search tool that:

- Significantly reduces irrelevant listings in search results.
- Offers a user-friendly interface for complex real estate searches.
- Enhances the overall user experience in finding the right property.
