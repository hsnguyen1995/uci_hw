-- List the following details of each employee: employee number, last name, first name, gender, and salary.
SELECT employees.emp_no, employees.last_name, employees.first_name, employees.gender, salaries.salary
FROM employees
LEFT JOIN salaries ON
employees.emp_no = salaries.emp_no;

-- List employees who were hired in 1986.
SELECT * FROM employees
WHERE hire_date BETWEEN '1986-01-01' AND '1986-12-31';

-- List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name, and start and end employment dates.
SELECT dept.dept_no, dept.dept_name, dept_man.emp_no, emp.last_name, emp.first_name, dept_man.from_date, dept_man.to_date
FROM departments AS dept
INNER JOIN dept_manager AS dept_man ON
	dept.dept_no = dept_man.dept_no
INNER JOIN employees AS emp ON
	dept_man.emp_no = emp.emp_no;


-- List the department of each employee with the following information: employee number, last name, first name, and department name.
SELECT dept_emp.emp_no, emp.last_name, emp.first_name, dept.dept_name
FROM dept_emp
INNER JOIN employees AS emp ON
	dept_emp.emp_no = emp.emp_no
INNER JOIN departments AS dept ON
	dept_emp.dept_no = dept.dept_no;

-- List all employees whose first name is "Hercules" and last names begin with "B."
SELECT * FROM employees
WHERE first_name = 'Hercules' AND last_name LIKE 'B%';

-- List all employees in the Sales department, including their employee number, last name, first name, and department name.
SELECT emp.emp_no, emp.last_name, emp.first_name, dept.dept_name
FROM employees AS emp
INNER JOIN dept_emp ON
	emp.emp_no = dept_emp.emp_no
INNER JOIN departments AS dept ON
	dept_emp.dept_no = dept.dept_no
WHERE dept.dept_name = 'Sales';

-- List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.
SELECT emp.emp_no, emp.last_name, emp.first_name, dept.dept_name
FROM employees AS emp
INNER JOIN dept_emp ON
	emp.emp_no = dept_emp.emp_no
INNER JOIN departments AS dept ON
	dept_emp.dept_no = dept.dept_no
WHERE dept.dept_name = 'Sales' OR dept.dept_name = 'Development';

-- In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.
SELECT last_name, COUNT(last_name) AS "Frequency Count of Employee Last Names"
FROM employees
GROUP BY last_name
ORDER BY "Frequency Count of Employee Last Names" DESC;