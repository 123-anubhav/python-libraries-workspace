import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]
sales = [10000, 15000, 12000, 18000]

#  **************************          LINE CHART    **************************************
plt.plot(months, sales, label="Sales",marker="o",color="red",linestyle="--")
plt.title("Sales by month")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()    #separate by diff values data unique
plt.grid(True)  # use for grid in charts
plt.show()

#  **************************          BAR CHART    **************************************

plt.bar(months, sales)

plt.title("Sales by month")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

#  **************************          BAR CHART With Horizontal Display    **************************************

plt.barh(months, sales)

plt.title("Sales by month")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

#  **************************          PIE CHART    **************************************

courses = ["Python", "Java", "DevOps", "AWS"]
students = [50, 40, 30, 35]

plt.pie(students,autopct="%1.2f%%",labels=courses)
plt.title("Student % Course Wise")
plt.xlabel("Courses")
plt.ylabel("students")
plt.legend()
plt.grid(True)
plt.show()


#  **************************          PIE CHART    **************************************

study_hours = [1, 2, 3, 4, 5]
marks = [35, 45, 60, 75, 90]

plt.scatter(study_hours, marks)

#plt.scatter(study_hours, marks,linewidths=10,color="red")
plt.title("Study Hours vs Marks ",color="blue")
plt.xlabel("Study Hours ",color="blue")
plt.ylabel("Marks",color="blue")
#plt.legend()
#plt.grid(True)
plt.show()

#  **************************          HISTOGRAM CHART    **************************************

marks = [35, 45, 50, 60, 65, 70, 75, 80, 85, 90, 95]

plt.hist(marks)
plt.title("Marks Distribution",color="blue")
plt.xlabel("Marks",color="red")
plt.ylabel("Number of Students",color="red")
plt.grid(True)
plt.show()