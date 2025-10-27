# Setup Instructions for GitHub and DockerHub

## Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. Create a new repository named `qr-code-generator`
3. Choose whether to make it public or private
4. Do NOT initialize with README (we already have one)
5. Click "Create repository"

## Step 2: Push to GitHub

```bash
cd /Users/krkaushikkumar/Desktop/IS601_Module7

# Add remote origin (replace YOUR-USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR-USERNAME/qr-code-generator.git

# Push to GitHub
git branch -M main
git push -u origin main
```

Verify the push was successful by checking your GitHub repository.

## Step 3: Setup DockerHub

1. Go to https://hub.docker.com/ and sign up for a free account
2. Go to Account Settings > Security > Personal Access Tokens
3. Click "Generate New Token"
4. Give it a name like "github-actions"
5. Select "Read & Write" permissions
6. Generate the token and **copy it**

## Step 4: Setup GitHub Secrets

1. Go to your GitHub repository settings
2. Navigate to "Secrets and variables" > "Actions"
3. Click "New repository secret"
4. Add secret `DOCKERHUB_USERNAME` with your DockerHub username
5. Add secret `DOCKERHUB_TOKEN` with the token you generated in Step 3

## Step 5: Manual Docker Push to DockerHub

If you want to push the Docker image manually before using GitHub Actions:

```bash
# Login to DockerHub
docker login

# Tag the image (replace YOUR-USERNAME with your DockerHub username)
docker tag qr-code-generator-app YOUR-USERNAME/qr-code-generator-app

# Push to DockerHub
docker push YOUR-USERNAME/qr-code-generator-app
```

## Step 6: GitHub Actions Trigger

Once the secrets are configured, the GitHub Actions workflow will:
- Automatically build the image when you push to main
- Run tests on the image
- Push the image to DockerHub

You can also manually trigger the workflow by making a commit and pushing:

```bash
# Make a small change (or just create an empty commit)
git commit --allow-empty -m "Trigger GitHub Actions workflow"
git push origin main
```

## Verification

1. **GitHub Repository**: Check that all files are present at https://github.com/YOUR-USERNAME/qr-code-generator
2. **GitHub Actions**: Go to Actions tab and verify the workflow ran successfully
3. **DockerHub**: Go to https://hub.docker.com/r/YOUR-USERNAME/qr-code-generator to see your pushed image

## Submitting Assignment

For submission, provide:
1. GitHub Repository Link: `https://github.com/YOUR-USERNAME/qr-code-generator`
2. DockerHub Image Link: `https://hub.docker.com/r/YOUR-USERNAME/qr-code-generator-app`
3. Screenshots:
   - Container logs showing successful execution
   - GitHub Actions workflow showing successful build and push
4. This repository link and the reflection document

---

**Note**: Replace `YOUR-USERNAME` with your actual GitHub and DockerHub username.
