# Contributing to VaultX

Thank you for considering contributing to VaultX! This document outlines the process for contributing to this project.

## How to Contribute

1. Fork the repository
2. Create a new branch for your feature or fix
3. Make your changes
4. Ensure your code follows the project's coding standards
5. Add tests for any new functionality
6. Submit a pull request

## Branch Naming Convention

Use the following format for branch names:
- `feature/<area>-<name>` for new features
- `bugfix/<area>-<name>` for bug fixes
- `docs/<area>-<name>` for documentation changes
- `refactor/<area>-<name>` for code refactoring

Examples:
- `feature/activities-add-filter`
- `bugfix/auth-token-expiry`
- `docs/api-update-endpoints`

## Pull Request Rules

1. Keep PRs focused on a single change or feature
2. Write clear, descriptive titles and descriptions
3. Reference any related issues in the description
4. Ensure all tests pass before submitting
5. Follow the code style of the existing codebase
6. Do not commit `.env` files or other secrets
7. Keep dependencies up to date where possible

## Coding Standards

### Backend (Python)
- Follow PEP 8 style guide
- Use type hints where possible
- Keep functions small and focused
- Write docstrings for public functions and classes
- Use meaningful variable names

### Frontend (TypeScript/React)
- Use functional components with hooks
- Follow TypeScript strict mode
- Extract reusable components
- Use meaningful component and variable names
- Keep CSS classes semantic where possible

## Testing

### Backend
- Write unit tests using pytest
- Test both positive and negative cases
- Mock external dependencies
- Aim for high test coverage on critical paths

### Frontend
- Write unit tests using Vitest and React Testing Library
- Test component rendering and user interactions
- Mock API calls
- Test accessibility where applicable

## Documentation

- Update documentation when changing functionality
- Keep README up to date with setup instructions
- Update API documentation when endpoints change
- Document any new environment variables

## Reporting Issues

When reporting issues, please include:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Screenshots if applicable
- Environment details (OS, browser versions)

## License

By contributing to VaultX, you agree that your contributions will be licensed under the project's license.