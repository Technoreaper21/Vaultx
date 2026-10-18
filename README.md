# VaultX

VaultX helps rural Indian students (Class 9 to graduation) discover skills, plan learning, and complete real opportunities (scholarships, apprenticeships), with teacher facilitators and verified mentors.

This is a basic-to-medium working skeleton built for the Citi India Hackathon.

## Table of Contents

- [Overview](#overview)
- [What Works vs Placeholder](#what-works-vs-placeholder)
- [Setup Instructions](#setup-instructions)
- [Project Structure](#project-structure)
- [Running the Application](#running-the-application)
- [Testing](#testing)
- [Development Guidelines](#development-guidelines)
- [License](#license)

## Overview

VaultX consists of:
- **Frontend**: React + TypeScript + Vite PWA with Tailwind CSS, i18next (English/Hindi)
- **Backend**: Python 3.12+ FastAPI with SQLAlchemy 2.0, Alembic, pydantic-settings
- **Data**: JSON placeholder data for activities, careers, opportunities
- **Infrastructure**: Docker Compose with PostgreSQL (pgvector)
- **CI/CD**: GitHub Actions workflow for linting and testing
- **Documentation**: Architecture guide and OpenAPI spec

## What Works vs Placeholder

| Component | Status | Details |
|-----------|--------|---------|
| **Backend API** | ✅ Works | `/health` endpoint returns status |
| **Auth Login** | ✅ Works (Stub) | Returns fake token based on username (student/facilitator/mentor/admin) |
| **Activities Endpoint** | ✅ Works | Returns placeholder activities data |
| **Careers Endpoint** | ✅ Works | Returns placeholder careers data |
| **Opportunities Endpoint** | ✅ Works | Returns placeholder opportunities with eligibility rules |
| **Sync Endpoint** | ✅ Works | Idempotent push using client-generated IDs (in-memory store) |
| **Eligibility Engine** | ✅ Works | Pure Python function evaluates rules with explanations |
| **Frontend App** | ✅ Works | Basic UI with navigation and placeholder data display |
| **Language Toggle** | ✅ Works | Switches between English and Hindi (placeholder translations) |
| **Database Integration** | ⏳ Placeholder | Docker Compose includes PostgreSQL but API uses in-memory for stubs |
| **Actual Tailwind CSS** | ⏳ Placeholder | Basic CSS utility classes in index.css (to be replaced with Tailwind) |
| **Dexie IndexedDB** | ⏳ Placeholder | Mentioned in architecture but not implemented |
| **PWA Features** | ⏳ Placeholder | Manifest and service worker to be configured with vite-plugin-pwa |
| **OpenAPI Spec** | ✅ Works | Exported OpenAPI 3.0 document in docs/api/openapi.yaml |
| **Real Data** | ❌ Placeholder | All data is clearly marked with `is_placeholder: true` and `source_url: null` |
| **LLM Gateway** | ❌ Placeholder | Described in architecture but not implemented (will only explain, never decide) |

## Setup Instructions

### Prerequisites

- **WSL2 Ubuntu** or Linux environment
- **Node.js** v18+ (we use v24.21.0)
- **npm** v9+ (we use v11.19.0)
- **Python** 3.12+ (we use 3.14.4)
- **Docker** v20+ (we use 29.1.3)
- **Git**

### Backend Setup

```bash
# Navigate to backend directory
cd apps/api

# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Copy environment example (optional)
cp .env.example .env
# Edit .env if needed (DATABASE_URL, SECRET_KEY)
```

### Frontend Setup

```bash
# Navigate to frontend directory
cd ../web

# Install dependencies
npm ci
```

### Environment Variables

Create `.env` files from the examples:
- `apps/api/.env` (from `.env.example`)
- `apps/web/.env.example` (for frontend vars if needed)

### Database Setup

The docker-compose file includes PostgreSQL with pgvector extension.
To start the database:
```bash
docker compose up -d db
```

## Running the Application

### Development Mode

#### Backend (API)
```bash
cd apps/api
source .venv/bin/activate
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```
API will be available at http://localhost:8000

#### Frontend (Web)
```bash
cd ../web
npm run dev
```
Frontend will be available at http://localhost:3000

#### Using Docker Compose
```bash
# From project root
docker compose up --build
```
This will start:
- db: http://localhost:5432 (PostgreSQL)
- api: http://localhost:8000
- web: http://localhost:3000 (served via nginx)

### Production Build

#### Frontend
```bash
cd apps/web
npm run build
```
Output goes to `apps/web/dist`

#### Backend
The Dockerfile produces a production-ready image.

## Testing

### Backend Tests
```bash
cd apps/api
source .venv/bin/activate
python -m pytest tests/ -v
```

### Frontend Tests
```bash
cd apps/web
npm test
```

### Linting

Backend linting (flake8) and frontend linting (ESLint) are configured in CI.

## Project Structure

```
Vaultx/
├── apps/
│   ├── api/                   # FastAPI backend
│   │   ├── app/               # Main application
│   │   │   ├── api/           # API endpoints
│   │   │   │   └── v1/        # Version 1 endpoints
│   │   │   ├── core/          # Configuration and security
│   │   │   ├── db/            # Database models and session
│   │   │   ├── rules/         # Business logic (eligibility)
│   │   │   └── tests/         # Unit tests
│   │   ├── alembic/           # Database migrations
│   │   ├── requirements.txt   # Python dependencies
│   │   ├── Dockerfile         # Container definition
│   │   └── .env.example       # Environment variables example
│   └── web/                   # React frontend
│       ├── src/               # Source code
│       │   ├── components/    # UI components
│       │   ├── i18n/          # Internationalization files
│       │   ├── __tests__/     # Unit tests
│       │   ├── App.tsx        # Main app component
│       │   └── main.tsx       # Entry point
│       ├── public/            # Static assets
│       ├── index.html         # HTML template
│       ├── package.json       # Node.js dependencies
│       ├── tsconfig.json      # TypeScript configuration
│       └── vite.config.ts     # Vite configuration
├── data/                      # JSON placeholder data
│   ├── activities.json
│   ├── careers.json
│   └── opportunities.json
├── docs/
│   ├── architecture.md        # Detailed architecture
│   └── api/
│       └── openapi.yaml       # API specification
├── docker-compose.yml         # Multi-service deployment
├── .github/
│   ├── workflows/             # CI/CD pipelines
│   │   └── ci.yml
│   └── pull_request_template.md
├── CONTRIBUTING.md            # Contribution guidelines
└── README.md                  # This file
```

## Running the Application (Quick Start)

```bash
# Clone repository
git clone <repository-url>
cd Vaultx

# Start services with Docker Compose (recommended for full stack)
docker compose up --build

# Or run separately for development:
# Terminal 1: Backend
cd apps/api
source .venv/bin/activate
uvicorn app.main:app --reload

# Terminal 2: Frontend
cd ../web
npm run dev
```

## API Endpoints

- `GET /health` - Health check
- `POST /auth/login` - Stub authentication (returns role)
- `GET /activities` - List of activities
- `GET /careers` - List of careers
- `GET /opportunities` - List of opportunities with eligibility rules
- `POST /sync/push` - Idempotent sync push

## What's Not Implemented (Placeholders)

- Real database connections (using in-memory stubs)
- Actual Tailwind CSS configuration (using basic CSS utility classes)
- Dexie IndexedDB for offline storage
- PWA service worker implementation
- Real LLM gateway (only explained in architecture)
- Facilitator and mentor dashboards
- Real authentication with database persistence
- Actual opportunity applications and activity responses
- Real eligibility rules from verified sources
- Installable PWA functionality

## License

This project is built for the Citi India Hackathon. See LICENSE file for details.

---

Built with ❤️ for rural Indian students' skill development.