# VaultX Architecture

## Overview
VaultX is a progressive web application (PWA) designed to help rural Indian students discover skills, plan learning, and find real opportunities like scholarships and apprenticeships. The platform consists of a frontend web application and a backend API, with local data storage for offline capability.

## Components

### 1. PWA Frontend (React + TypeScript + Vite)
- **Framework**: React 18 with TypeScript
- **Build Tool**: Vite for fast development and building
- **Styling**: Tailwind CSS (via utility classes in index.css for now)
- **Internationalization**: i18next with English and Hindi placeholder translations
- **State Management**: React hooks and context (minimal for this skeleton)
- **Offline Storage**: Dexie.js setup for IndexedDB (to be implemented)
- **Routing**: React Router v6 for SPA navigation
- **PWA Features**: Vite plugin for PWA (manifest, service worker) - to be configured

### 2. Backend API (Python + FastAPI)
- **Framework**: FastAPI for high-performance async API
- **Language**: Python 3.12+
- **Database**: PostgreSQL with SQLAlchemy 2.0 ORM
- **Migrations**: Alembic for schema management
- **Validation**: Pydantic models for request/response validation
- **Security**: JWT-based authentication with password hashing (passlib)
- **Environment**: pydantic-settings for configuration management

### 3. Core Functionalities

#### Skill Discovery
- Frontend fetches activities from `/api/v1/activities/`
- Activities are displayed in a grid with placeholder data
- Each activity includes title, description, and placeholder flag

#### Learning Plans
- Frontend fetches careers from `/api/v1/careers/`
- Careers shown with descriptions and placeholder flags
- Future: Learning path generation based on skills and interests

#### Opportunities
- Frontend fetches opportunities from `/api/v1/opportunities/`
- Each opportunity includes eligibility rules as JSON
- Eligibility evaluation done in pure Python rules engine
- Placeholder data with fake eligibility rules

#### Teacher Facilitators & Mentors
- Role-based access via JWT tokens (student, facilitator, mentor, admin)
- Login endpoint returns role based on username (stub)
- Future: Facilitators can create/manage activities, mentors guide students

#### Offline Sync
- IndexedDB (Dexie) for local storage of activities, careers, opportunities
- Sync queue for offline actions (responses, applications)
- `/sync/push` endpoint for idempotent sync using client-generated IDs
- Conflict resolution strategy: last write wins (to be implemented)

#### Rules Engine
- Pure Python function in `apps/api/app/rules/eligibility.py`
- Evaluates eligibility criteria: age, grade, subjects, education, gender
- Returns detailed pass/fail with explanations per criterion
- Designed to be explainable, not decision-making (LLM gateway only explains)

#### LLM Gateway
- Placeholder for future integration
- Will only provide explanations, never make eligibility decisions
- Ensures transparency and trust in the system

### 4. Data Flow
1. User accesses PWA via browser (installable)
2. Service worker caches static assets for offline use
3. On first load, app fetches data from API (or loads from IndexedDB if available)
4. User interactions (e.g., applying for opportunity) are stored locally
5. When online, changes are synced to backend via `/sync/push`
6. Backend validates and stores data in PostgreSQL
7. Eligibility checked via rules engine before granting access to opportunities

### 5. Development Setup
- **Backend**: Virtual environment at `apps/api/.venv`, dependencies in `requirements.txt`
- **Frontend**: Node.js dependencies in `apps/web/package.json`
- **Database**: PostgreSQL with pgvector extension (docker-compose)
- **API Docs**: OpenAPI specification exported from FastAPI (to be generated)

### 6. Security Considerations
- No real secrets in repository (uses .env.example)
- Passwords hashed with bcrypt
- JWT tokens with expiration
- CORS configuration needed for production
- Input validation via Pydantic models
- Placeholder data clearly marked with `is_placeholder: true`

### 7. Future Enhancements
- Implement Dexie for IndexedDB storage
- Add actual Tailwind CSS configuration
- Connect to real PostgreSQL database
- Generate OpenAPI spec from FastAPI endpoints
- Add unit and integration test coverage
- Implement real authentication with database-backed users
- Add LLM gateway for explanations (not decisions)
- Enhance eligibility rules with more complex criteria
- Add facilitator and mentor dashboards