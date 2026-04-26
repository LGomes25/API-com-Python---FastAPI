# GitHub Copilot Instructions for FastAPI Blog Project

## Project Structure & Conventions
- Follow the folder structure: controllers (routes/business logic), schemas (Pydantic validation/types), views (response models), services (auxiliary logic), models (data models if needed).
- Entry point must be `main.py` at the project root.
- Use static typing (type hints) everywhere.
- Use English for code (variables, functions, files), Portuguese for documentation/examples if needed.
- Follow PEP8 for code style.

## FastAPI Usage
- Use `APIRouter` for route modularization.
- Always set `response_model` in endpoints.
- Prefer `Annotated` for optional/validated parameters.
- Document endpoints and parameters with clear docstrings.

## Schemas & Validation
- Use Pydantic for all input/output schemas.
- Use `Field` for defaults, validation, and descriptions.
- Separate input (`PostIn`) and output (`PostOut`) schemas.

## Best Practices
- Do not store sensitive/production data in in-memory lists.
- Use comments for didactic or non-trivial code.
- Keep code clean, modular, and reusable.
- Write automated tests for endpoints when possible.

## Project Conventions
- Treat the project as didactic, but use professional practices.
- Update documentation with relevant changes.

---

### Example Prompts
- "Add a new endpoint following controllers/schemas pattern."
- "Implement a validation schema for a new resource."
- "Refactor to move business logic to services."
- "Update docs per project conventions."

---

### Future Customizations
- Add instructions for automated tests.
- Define database integration standards.
- Add authentication/authorization guidelines.
- Specify API versioning patterns.
