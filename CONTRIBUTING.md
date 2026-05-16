# Contributing to MenuNest

Thank you for your interest in contributing to MenuNest: AI Copilot for Food Entrepreneurs!

## Project Overview

MenuNest is an AI-powered web application built with Streamlit that helps food entrepreneurs turn early business ideas into practical launch plans. The project was created for the IBM Bob Hackathon and demonstrates AI-assisted development workflows.

## How to Contribute

### Reporting Issues

If you find a bug or have a feature suggestion:

1. Check if the issue already exists in the GitHub Issues
2. If not, create a new issue with:
   - Clear title and description
   - Steps to reproduce (for bugs)
   - Expected vs. actual behavior
   - Screenshots if applicable
   - Your environment details (OS, Python version, browser)

### Suggesting Features

We welcome feature suggestions! Please:

1. Check existing issues and discussions first
2. Create a new issue with the "enhancement" label
3. Describe the feature and its use case
4. Explain how it benefits food entrepreneurs

### Code Contributions

#### Getting Started

1. Fork the repository
2. Clone your fork locally:
   ```bash
   git clone https://github.com/your-username/menunest-ai-copilot.git
   cd menunest-ai-copilot
   ```

3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Create a `.env` file from the example:
   ```bash
   cp .env.example .env
   ```

6. Run the app locally:
   ```bash
   streamlit run app.py
   ```

#### Development Workflow

1. Create a new branch for your feature or fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes following our coding standards (see below)

3. Test your changes thoroughly:
   ```bash
   pytest tests/
   ```

4. Commit your changes with clear, descriptive messages:
   ```bash
   git commit -m "Add feature: description of what you added"
   ```

5. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

6. Create a Pull Request with:
   - Clear title and description
   - Reference to related issues
   - Screenshots/demos if applicable
   - Test results

#### Coding Standards

- **Python Style**: Follow PEP 8 guidelines
- **Type Hints**: Use type hints for function parameters and returns
- **Docstrings**: Add docstrings to all functions and classes
- **Comments**: Write clear comments for complex logic
- **Imports**: Organize imports (standard library, third-party, local)
- **Line Length**: Keep lines under 88 characters (Black formatter standard)

#### Code Structure

```
src/
├── config.py           # Configuration and constants
├── prompt_builder.py   # AI prompt construction
├── ai_generator.py     # AI integration logic
├── validators.py       # Input and output validation
├── report_renderer.py  # UI rendering components
├── export_utils.py     # Export functionality
└── sample_data.py      # Demo/fallback data
```

#### Testing

- Write tests for new features in the `tests/` directory
- Ensure all tests pass before submitting PR
- Include both unit tests and integration tests where appropriate
- Test the demo mode functionality

#### Documentation

- Update README.md if you change functionality
- Add docstrings to new functions and classes
- Update type hints and comments
- Consider adding examples to `docs/` if needed

## IBM Bob Integration

This project was built with IBM Bob as an AI development partner. When contributing:

- Consider how IBM Bob could assist with your development workflow
- Document any IBM Bob sessions in `bob_sessions/` (if applicable)
- Follow the established patterns for AI-assisted development

## Food Industry Focus

Remember that MenuNest serves food entrepreneurs. When contributing:

- Consider the needs of small food businesses
- Think about practical, actionable outputs
- Keep the user experience simple and focused
- Consider cultural and regional food differences
- Ensure accessibility for non-technical users

## Community Guidelines

- Be respectful and inclusive
- Help newcomers get started
- Share knowledge and best practices
- Focus on constructive feedback
- Celebrate diverse perspectives in food entrepreneurship

## Questions?

- Open a GitHub Discussion for general questions
- Create an issue for specific bugs or features
- Check existing documentation in `docs/`

## License

By contributing to MenuNest, you agree that your contributions will be licensed under the MIT License.

---

Thank you for helping make MenuNest better for food entrepreneurs worldwide! 🍽️