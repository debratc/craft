#
import random
from datetime import datetime

projects = ["Project A", "Project B", "Project C", "Project D"]
print(f"{datetime.now()}: Dự án được chọn: {random.choice(projects)}")
