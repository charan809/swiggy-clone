import os

# Step 1: Create the CONTRIBUTORS.md file
def create_contributors_file():
    contributors_content = """
# Contributors to Swigi Clone Project

Thanks to all the contributors who made this project possible!

## 💻 Code Contributors

- [@aditya-singh](https://github.com/aditya-singh) - Lead Developer
- [@john-doe](https://github.com/john-doe) - UI/UX Designer
- [@jane-smith](https://github.com/jane-smith) - Backend Developer

## 🎨 Design Contributors

- [@alex-doe](https://github.com/alex-doe) - Logo Design
- [@emily-jones](https://github.com/emily-jones) - App UI Design

## 🤖 Test Contributors

- [@mike-lee](https://github.com/mike-lee) - Quality Assurance
- [@sara-kim](https://github.com/sara-kim) - Manual Testing

## 🎉 Special Thanks

- [@swiggy](https://github.com/swiggy) for the inspiration and API documentation

If you'd like to contribute to this project, feel free to open a pull request!
"""

    # Save the CONTRIBUTORS.md file
    with open('CONTRIBUTORS.md', 'w') as file:
        file.write(contributors_content)
    print("CONTRIBUTORS.md file created.")


# Step 2: Update README.md to include the link to CONTRIBUTORS.md
def update_readme():
    with open('README.md', 'a') as file:
        file.write("\n## Contributors\n")
        file.write("We love and appreciate all the contributions to the Swigi Clone! Please check out our [Contributors Page](CONTRIBUTORS.md) to see the amazing individuals who have helped make this project a success!\n")
        file.write("If you would like to become a contributor, feel free to [open an issue](https://github.com/your-repo/issues) or submit a pull request!\n")
    print("README.md updated to include Contributors link.")


# Step 3: Optionally, automate contributors using All-Contributors Bot
def add_contributors_with_all_contributors():
    # Instructions to add contributors using the All-Contributors bot.
    print("If you'd like to automate contributor recognition, run the following commands in your terminal:")
    print("1. Install All-Contributors CLI:")
    print("   npm install -g all-contributors-cli")
    print("2. Add contributors:")
    print("   npx all-contributors-cli add @your-username code")
    print("3. Generate contributor section:")
    print("   npx all-contributors-cli generate")
    print("These steps will automatically add contributors and generate the CONTRIBUTORS.md file.")


# Main execution
def main():
    # Ensure the project has a README file before proceeding
    if not os.path.exists('README.md'):
        print("Error: README.md file does not exist!")
        return

    # Step 1: Create CONTRIBUTORS.md file
    create_contributors_file()

    # Step 2: Update README.md with the contributors link
    update_readme()

    # Step 3: Provide instructions for automating contributor recognition
    add_contributors_with_all_contributors()


# Run the script
if __name__ == "__main__":
    main()
