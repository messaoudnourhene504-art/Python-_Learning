# Simple Task Manager Tool
# Created by: messaoudnourhene504-art
# License: MIT

def main():
    tasks = []
    
    while True:
        print("\n" + "="*30)
        print("   DAILY TASK MANAGER   ")
        print("="*30)
        print("1. Add New Task")
        print("2. View All Tasks")
        print("3. Clear All Tasks")
        print("4. Exit")
        print("="*30)

        choice = input("Select an option (1-4): ").strip()

        if choice == '1':
            new_task = input("Enter the task: ").strip()
            if new_task:
                tasks.append(new_task)
                print("✅ Task added successfully!")
            else:
                print("⚠️ Cannot add an empty task.")
        
        elif choice == '2':
            print("\n📋 YOUR CURRENT TASKS:")
            if not tasks:
                print("Your list is empty.")
            else:
                for i, t in enumerate(tasks, 1):
                    print(f"{i}. {t}")
        
        elif choice == '3':
            confirm = input("Are you sure? (yes/no): ").strip().lower()
            if confirm == 'yes':
                tasks.clear()
                print("🗑️ All tasks have been deleted.")
        
        elif choice == '4':
            print("Thank you for using the tool. Happy Coding!")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
