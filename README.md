# Hiver AI Support Agent

An AI-powered customer support prototype built using the Customer Support on Twitter dataset.

## 1. Project Overview

This project builds a customer-support agent for AppleSupport.

The system performs three main tasks:

1. Classifies incoming customer messages into support intents.
2. Retrieves similar historical AppleSupport responses.
3. Decides whether the issue can be auto-handled or should be escalated to a human.

## 2. System Pipeline

Customer Message
        ↓
Intent Classification
        ↓
Historical Support Retrieval
        ↓
Grounded Reply Draft
        ↓
Auto-handle / Escalate Decision

## 3. Dataset

The primary dataset is the Customer Support on Twitter dataset from Kaggle.

The project focuses on the AppleSupport brand.

The complete raw dataset is not stored in this repository because of its large size.

The required dataset can be downloaded separately and placed inside the `data/` directory.

## 4. Intent Categories

The initial support taxonomy contains:

- `ios_update`
- `battery_charging`
- `audio_headphone`
- `apple_music`
- `activation_account`
- `apps_software`
- `device_performance`
- `other_general_support`

These categories were derived from recurring themes observed in AppleSupport customer messages.

## 5. Project Structure

```text
Hive_AI_Support_Agent/
│
├── data/
├── golden_set/
├── reports/
├── results/
├── src/
└── .gitignore
