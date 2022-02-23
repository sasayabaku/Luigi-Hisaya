from genericpath import exists
import os

import luigi

fileA = './tmp/Sample1_TaskA.txt'
fileB = './tmp/Sample1_TaskB.txt'
textA = "TaskA SUCCEEDED"

path = './tmp/'

log_dir = './tmp/luigi/log'

class TaskX(luigi.Task):
    """
    TaskX class
    """

    def requires(self):
        return []
        # 先行するタスクがない場合は、空リストのまま、ある場合はタスク名記載

    def output(self):
        # ログファイルを生成 
        # !! outputで指定したファイルの有無で実行判断を行っている
        os.makedirs(os.path.join(log_dir), exist_ok=True)

        return luigi.LocalTarget(os.path.join(log_dir, 'taskX'))

    def run(self):

        os.makedirs(path, exist_ok=True)

        with open(fileA, 'w') as f:
            f.write(textA)
        
        with self.output().open('w') as out_file:
            out_file.write("")

if __name__ == '__main__':
    luigi.run()