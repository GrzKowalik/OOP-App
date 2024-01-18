class TaskManager:
    def __init__(self):
        self.task_dict = {}
        self.current_id = 1

    def add_task(self, task):
        """Method to add a task to the task_dict"""
        self.task_dict[self.current_id] = task
        self.current_id += 1

    def remove_task(self, task_id):
        """Method to delete a task from the task_dict and update keys in the task_dict"""
        if task_id not in self.task_dict:
            print("Task with this ID doesn't exist")
            return

        del self.task_dict[task_id]
        for key in list(self.task_dict.keys()):
            if key > task_id:
                self.task_dict[key - 1] = self.task_dict.pop(key)
        self.current_id -= 1

    def show_tasks(self):
        """Method to show all task IDs and tasks in the task_dict"""
        if not self.task_dict:
            self.show_empty_tasks()
        else:
            for task_id, task in self.task_dict.items():
                print(f'{task_id} : {task}')
            print()

    @staticmethod
    def show_empty_tasks():
        """Static method to show an empty task_dict"""
        print('Your to-do list is empty\n')

    @staticmethod
    def print_info():
        print("What do you want to do?")
        print("1. ADD TASK")
        print("2. DELETE TASK")
        print("3. SHOW TASKS")
        print("Q. EXIT\n")


class Main:
    @staticmethod
    def main():
        task_manager = TaskManager()

        while True:
            task_manager.print_info()
            answer = input('Choose the action number you want to perform (1/2/3/Q): ')
            if answer == '1':
                task = input('Enter the task you want to add to the list: ')
                task_manager.add_task(task)
            elif answer == '2':
                task_manager.show_tasks()
                task_id_to_remove = int(input('Enter the task number you want to delete: '))
                task_manager.remove_task(task_id_to_remove)
            elif answer == '3':
                task_manager.show_tasks()
            elif answer.upper() == 'Q':
                print('End')
                break
            else:
                print(f'You entered an incorrect value: {answer}')
                retry = input('Do you want to try again or exit? (YES/NO): ')
                if retry.upper() == 'YES':
                    print('Restarting...')
                    continue
                elif retry.upper() == 'NO':
                    print('End')
                    break


if __name__ == '__main__':
    Main.main()
