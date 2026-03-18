# Copilot Coding Standards (Expense Sharing Backend)

This document defines **non-negotiable engineering standards** for all generated and edited code in this repository.

## 1) Core Principles

- Follow **OOP** fundamentals: clear abstractions, encapsulation, and explicit boundaries.
- Enforce **SOLID**:
	- **S**ingle Responsibility: each class/function has one reason to change.
	- **O**pen/Closed: extend with new strategy/policy classes, avoid modifying stable code.
	- **L**iskov Substitution: interchangeable strategy implementations.
	- **I**nterface Segregation: small focused contracts.
	- **D**ependency Inversion: depend on abstractions, not concrete infrastructure.
- Keep code **lean, cohesive, and loosely coupled**.
- Prefer readability and maintainability over cleverness.
- Follow **DRY (Don’t Repeat Yourself)**: eliminate duplication in domain logic, validation, mapping, and test setup.
- Apply the **Boy Scout Rule**: leave touched code cleaner than you found it.

## 1.1) Development Workflow (TDD Mandatory)

- Use **TDD by default** for business/service/domain changes.
- Follow **Red → Green → Refactor** strictly:
	1. Write a failing test describing behavior.
	2. Implement the minimal code to pass.
	3. Refactor while keeping tests green.
- Do not add production logic without a corresponding failing test first (unless fixing urgent production breakage).
- Keep each TDD cycle small and focused on one behavior.

## 1.2) Unit Testing Style (Chicago School)

- Prefer **Chicago-style** unit tests:
	- Test through public interfaces with real domain objects where practical.
	- Verify observable outcomes and state changes, not collaborator call counts.
	- Use test doubles only at true boundaries (external I/O, gateways, third-party services).
- Avoid London-style over-mocking in domain/service tests.
- Favor expressive test names that describe behavior in business terms.

## 2) Function & Class Size Constraints

- Target function length: **3-5 lines**.
- Hard upper bound: **8 lines for the majority of functions**.
- If a function grows beyond 8 lines, split into private helpers.
- Use descriptive names so helpers remain intention-revealing.
- Classes should be small and role-focused.

## 3) Architecture & Patterns

- Preserve and strengthen layered architecture:
	- **View/API layer**: transport concerns only.
	- **Service layer**: orchestration + business rules.
	- **Repository layer**: persistence concerns only.
	- **Strategy/Factory**: runtime behavior selection.
- Apply patterns only when they reduce coupling or simplify extension:
	- Strategy, Factory, Repository, Mapper/Adapter, Policy.
- Avoid God classes and deep inheritance hierarchies.

## 4) Style Rules

- No one-letter variable names.
- No dead code, commented-out code, or duplicate logic.
- Avoid inline comments unless explaining non-obvious domain constraints.
- Keep public APIs stable unless a change is explicitly requested.
- Raise domain-specific errors with clear messages.
- When touching any file, apply small opportunistic cleanups that reduce complexity without changing behavior.

## 5) Testing Standards (Mandatory)

- Aim for **100% unit test coverage** for changed/added domain logic.
- Tests must cover **behaviors**, not implementation details.
- Write the test first and ensure it fails before implementing behavior.
- Use Arrange-Act-Assert structure.
- Test only public behavior/outcomes:
	- returned values
	- state transitions
	- side effects at boundaries
	- raised errors
- Do not assert private method calls or internal data structure layout.
- Add edge-case tests for invalid inputs and boundary conditions.
- Keep tests deterministic, isolated, and fast.

## 6) Dependency & Coupling Rules

- Inject collaborators (repositories, policies, strategies) where practical.
- Keep framework-specific code at edges; keep core domain framework-light.
- Prefer composition over inheritance.
- Prevent cyclic dependencies across modules.

## 7) Change Checklist (Copilot must satisfy before finishing)

For every code change, ensure all are true:

1. Functions are 3-5 lines when feasible; most are <= 8 lines.
2. Classes have single responsibility and high cohesion.
3. New behavior is extensible via abstractions/patterns.
4. TDD was followed: failing test first, then minimal implementation, then refactor.
5. Tests validate behavior (Chicago style) and include meaningful edge cases.
6. Coverage for touched logic is at or moving toward 100%.
7. No duplicated logic or unnecessary complexity introduced.
8. Touched areas are cleaner after the change (Boy Scout Rule).

## 8) Refactoring Guidance

When code violates these rules, prioritize:

1. Extract function to meet line/clarity limits.
2. Introduce/strengthen interface boundaries.
3. Move persistence logic out of services into repositories.
4. Replace condition-heavy branching with strategy/policy patterns.
5. Add/adjust behavior-focused tests.
6. Remove duplication by extracting shared abstractions/utilities where appropriate.
7. Apply small cleanup improvements in touched files.

## 9) Definition of Done

A task is done only when:

- Design follows OOP + SOLID.
- Code is concise, cohesive, and loosely coupled.
- TDD cycle was respected for business/domain behavior.
- Unit tests follow Chicago style and assert outcomes, not internals.
- Majority of functions are <= 8 lines (target 3-5).
- Tests are behavior-oriented and comprehensive.
- The project remains clean: tests pass and no new warnings/errors are introduced.
