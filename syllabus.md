## Syllabus

# NESC 3505

## Neural Data Science
*Cross-Listed as PSYO 3505*
### Summer 2020, version 0.6, 2020-05-27
Course will run July 6 – August 24, 2020
**DRAFT: subject to change prior to start of the course**


#### Instructor
Dr. Aaron Newman
Email: [Aaron.Newman@dal.ca](mailto:Aaron.Newman@dal.ca)

#### Teaching Assistant
TBD

## Recognition of Mi’kmaq Territory
Dalhousie University would like to acknowledge that the University is on Traditional Mi’kmaq Territory. The Elders in Residence program provides students with access to First Nations elders for guidance, counsel and support. Visit the [Indigenous Student Centre](https://www.dal.ca/campus_life/communities/indigenous.html) or contact the programs at elders@dal.ca.

## Diversity and Inclusion – Culture of Respect
Every person at Dalhousie has a right to be respected and safe. We believe inclusiveness is fundamental to education. We stand for equality. Dalhousie is strengthened in our diversity. We are a respectful and inclusive community. We are committed to being a place where everyone feels welcome and supported, which is why our Strategic Direction prioritizes fostering a culture of diversity and inclusiveness. For more information please see [here](http://www.dal.ca/cultureofrespect.html).

# Course Description
An introduction to data management, manipulation, visualization, and analysis for neuroscience. Students will learn scientific programming in Python, and use this to work with example data from areas such as single-cell recording, EEG, and structural and functional MRI. Basic signal processing techniques including filtering will be covered.

## Prerequisites
__PSYO 2000__, __PSYO 2501__, and __NESC 2470__, with a minimum grade of B in PSYO 2501. Grades of B+ or better in all three classes are recommended. __No prior programming experience is required__.

# Background and Rationale
Most areas of neuroscience research and development rely on increasingly large and complex data sets. Discovery and application in neuroscience thus relies on the ability to manage these large data sets, and extract meaning from them. In other words, neuroscience now relies heavily on **data science**, which has been variously defined as “…an umbrella term to describe the entire complex and multistep processes used to extract value from data.” (Wing, 2019) and the ability to “bring structure to large quantities of formless data and make analysis possible” (Davenport & Patil, 2012, p.73).

__In neuroscience, data science is an increasingly necessary skill.__ Data from techniques like single-cell recordings, local field potentials, EEG, and fMRI is complex and multidimensional. Being able to understand, manipulate, and visualize the structure of these complex datasets is a necessary skill for performing the resaerch. On top of this, it is increasingly clear that very large data sets - often built collaboratively by many labs - are required to make reliable inferences about neuroscientific processes. Making inferences also depends on computational models - ways of identifying and representing patterns in the data. While some of these will be familiar from statistics class, a wide range of statistical and machine learning models are now widely used in neuroscience.

While data science and statistics are overlapping fields, statistics is generally focused on the specific task of testing hypotheses based on data. Data science more broadly includes the storage, manipulation, visualization, filtering, and preparation of data that is typically required prior to statistical analysis. Data Science does also encompass statistics, as well as machine learning; whereas statistics generally involves deriving conclusions from existing data, machine learning involves making predictions from a data set that will generalize to other data. Since statistics is covered in other courses in the neuroscience and psychology curricula, this course focuses instead on the other “front end” aspects of data science described above. Other areas of data science, including “back-end” data science (engineering, hardware, databases) and software development, will not be covered.

Central to data science is the ability to use scientific programming languages, such as Python, Matlab, and R. This ability includes a strong understanding of the fundamentals of at least one programming language, and the ability to extend one’s knowledge through continuous learning and problem-solving. This course teaches Python, a mature and widely-used language in neuroscience and data science more broadly. However, much of the fundamentals of scientific programming and data science are common to all many languages. Thus, having learned Python, you will be better-prepared to learn new languages in the future, as necessary.

Another important facet of data science is that it is a __team endeavour__. On the one hand, it is founded on open, shared software developed by widely distributed teams of contributors. On the other hand, the practice of data science typically involves teams of individuals with complementary skillsets, both due to the size and complexity of many projects. In science, these teams often comprise students and faculty members in collaborating labs distributed around the world. This class prepares you for such collaboration by developing and coaching your teamwork skills, as well as teaching you how to use software platforms that support such collaboration.

The skills learned in this class will benefit students working in a wide variety of areas of neuroscience. As well, the class will provide an introductory foundation in data science that can be applied to a wide range of areas of research and application, in academia, industry, and government.

#### References:
Davenport, T. H., & Patil, D. J. (2012). Data scientist. *Harvard business review*, 90(5), 70-76

Irizarry, R. A. (2020). The Role of Academia in Data Science Education. *Harvard Data Science Review*, 2(1). https://doi.org/10.1162/99608f92.dd363929

Wing, J. M. (2019). The data life cycle. *Harvard Data Science Review*. https://doi.org/10.1162/99608f92.e26845b4

# Learning Objectives
## Hard Skills
- extract meaning from data, but also articulate the limitations of the conclusions you can draw from it
- Write functional and efficient code in Python to perform basic data science tasks
- use GitHub for collaborative software development and project management
- Read and write data files in common formats such as CSV and Excel
- Organize and manipulate data structures
- Work with continuous, discrete, and factorial data
- Visualize data in a variety of graphical formats
- Perform exploratory data analysis using graphical and basic statistical operations
- Perform basic signal processing on data, such as filtering in temporal and spatial dimensions
- Build and run data processing pipelines on various types of neuroscientific data, including single unit recordings, time series, and 2D/3D/4D images
- Understand basic concepts and common tools used in machine learning, including deep neural networks
- extend your Python skills using online resources

## Soft Skills
- demonstrate a professional work ethic
- be effective and productive in a remote working environment
- work collaboratively, effectively, and productively in a distributed team
- manage projects: manage time and human resources effectively to achieve specific objectives on a stated timeline
- peer-review the work of other team members
- teach others skills and solutions you discover, and communicate your approach to discovering these
- articulate your strengths and weaknesses as a data scientist working in a team, and identify ways to improve your abilities
- demonstrate skills you have developed using a portfolio of work, to potential supervisors/employers
- use, and communicate the value of, open and reproducible code and data

# Class Format and Schedule
This class consists of the following components:
- Online lectures, lessons and tutorials
- Scheduled class time to work on assignments and get guidance from the teaching team

## Online lectures and tutorials
This course employs a “flipped classroom” model, and is designed to be offered in an online format. Lectures and tutorials are pre-recorded and available online for viewing at any time. Many of these lessons involve quizzes and coding activities. You are expected to complete assigned lessons prior to scheduled class times. **This course requires that you put in significant hours per week outside of class: at the outset, you should budget 16 h/week for a 7-week condensed summer version of the course, or 8 h/week for the regular term version.** This is in addition to 2-3 h/week of class time.

## Scheduled Class Time
Scheduled class times are devoted to working on assignments and projects, with the teaching team available for discussion and guidance. Students will be encouraged to present short tutorials explaining how they approached and solved different problems. In online delivery, these are held as group video sessions, with screen sharing. Classes involve assignments that build on the online lessons, so students who have not completed the online lessons prior to class time will not get much benefit from the class time. Participation in the scheduled classes is not mandatory, but strongly recommended. **Scheduled class times are the only times when the teaching team is available for live consultation on course work**. Questions submitted outside of class time may be addressed by the teaching team during class time.  

# Course Materials
All necessary materials will be provided online, either on or through Brightspace. **You must have access to a computer** running a recent version of the Mac, Windows, Chrome, or Linux operating systems. It is not possible to complete the course using only a mobile device (phone, tablet/iPad). **You must also have access to internet service** of sufficient quality to stream videos and maintain a live connection to remote servers. Provisions will be made if students cannot participate in live audio/video sessions due to internet constraints; please contact the instructor to discuss if this is an issue for you.

Beyond these basic requirements, this course emphasizes (and will teach you about) openly accessible resources including the software that runs the course, open access to the course materials, and the use of external resources that are available for free. No textbook is required. This course will rely on *Open Educational Resources* — materials that are freely accessible and openly licensed—including online tutorials, videos, and books. A wide variety of educational materials (free and paid) for data science are available, and this course teaches an approach to lifelong learning and exploration by which you will be able to find critically evaluate the information necessary to perform desired tasks.

# Assessment and Evaluation

Your final grade will be based on a combination of *formative assessments* (self and peer evaluations) and *summative evaluations* (presentations, assignments, projects). Each component is described below, followed by a table showing the number and point weighting of each.

## Formative Assessments
Formative assessments are designed to support you in improving your performance in the class, through self-assessment, peer assessment, and instructor feedback. These are designed to require little time to complete. The contribute a smaller proportion of your grade than evaluations (approximately 20%), but collectively can make a significant difference in your grade.

### Online Lessons
Online lessons are to be completed prior to class time. Deadlines are provided online. Each lesson is graded on a pass/fail basis, based on whether you complete the lesson or not. Lessons can be completed later than the posted due date, up to the last day of class, with no penalty. However, not completing lessons by the posted due dates will leave you unprepared for future classes and assignments. No points for lessons will be granted after the last day of class.

### Self Assessments
You will submit regular written assessments of your own learning progress over the term. Each should be 300-500 words in length.

### Peer Assessments
You will be asked to submit structured peer reviews following various group activities over the term (demo days and team projects). This will be done using a rubric asking for ratings of participation, preparation, communication, collaboration, and academic quality.

### Demos
These are group sessions in which each member demos something they learned/figured out in working on the assignments or projects.

### Meet 'n Greets

You will earn bonus points by participating in short (5-10 min) online one-on-one meetings with other class members. These are scheduled by students at your mutual convenience, and can take the form of a text-based chat or a video chat. The purpose of these is to allow for the kinds of casual interactions you might normally have with others in a face-to-face class, and allow you to get to know people as potential team members for projects. To protect everyone's safety, all students have the ability to block others anonymously, and may discontinue a meeting at any time without penalty. All students are expected to abide by [Dalhousie University's Code of Student Conduct](https://www.dal.ca/dept/university_secretariat/policies/student-life/code-of-student-conduct.html), and violations will be addressed through the procedures described there. Please report any inappropriate behaviour to the instructor immediately. You will be heard, and you will be respected.

## Summative Evaluations
Summative evaluations comprise the majority of your final grade (approximately 80%). All summative evaluations are graded. Because 20% of your final grade (the formative assessments) are "easy" pass/fail points, you can expect that grading of the summative evaluations will be quite strict.

### Assignments
These are coding assignments that you will complete, based on neuroscience data. There is an assignment due every week, except weeks when projects are due. Scheduled class time is the only time you will be able to get help on the assignments from the teaching team. There will be 6 assignments over the term. You must submit a minimum of 4 of these, but bonus points will be awarded for submitting 5 or 6.

Late work will be penalized 1% per hour, with the clock starting the minute after the deadline has elapsed. Requests for extensions will only be considered prior to the due date.

### Projects
There are 2 team-based projects to complete. These projects are directly based on the class assignments, but integrate across multiple classes and assignments, as well as requiring you to extend and apply what you have learned, to new contexts.

Late work will be penalized 1% per hour, with the clock starting the minute after the deadline has elapsed. Requests for extensions will only be considered prior to the due date.  

### Portfolio
One of the outcomes of this class is that you will have a portfolio demonstrating your work, that you could show to a potential employer or graduate supervisor. Building this will mostly happen in the context of your completing the course work (demos, projects, and assignments); assembling your portfolio simply means selecting what you feel best represents your work, and putting a bit of "packaging" around it. You will submit a first version midway through the course for feedback, and then a final version at the end of term.

### Demos
Demos are short demonstrations that you prepare to teach your fellow students. They can be videos (1-3 min) or written 500-1000 words). The goal is to share some insight or discovery with other students. This could be how you approached and solved some problem in an assignment, a review of a website or other resources you found helpful for the class, etc.. You will be rewarded for creativity in choice of topic and in delivery.

# Grading
This course follows the Dalhousie grading scale, but in a different way than you are probably used to. Borrowing the model of role-playing games (RPGs), you accumulate experience points (XP) by completing the assessments and evaluations listed above. Formative assessments are pass/fail, so you get the full XP for completing them. Summative evaluations are graded, so the XP you receive will be in proportion to your grade (e.g., if you get 70% on an assignment, you get 70% of the XP that the assignment is worth). Like RPGs, your XP determine your level in the course, according to the table below. Your level at the end of the course determines your final grade.

| Level | XP    | letter grade |
|-------|-------|--------------|
| 1     | 100   |              |
| 2     | 400   |              |
| 3     | 900   |              |
| 4     | 1600  |              |
| 5     | 2500  |              |
| 6     | 3600  |              |
| 7     | 4900  |              |
| 8     | 6400  |              |
| 9     | 8100  |              |
| 10    | 10000 |              |
| 11    | 12100 | D            |
| 12    | 14400 | C-           |
| 13    | 16900 | C            |
| 14    | 19600 | C+           |
| 15    | 22500 | B-           |
| 16    | 25600 | B            |
| 17    | 28900 | B+           |
| 18    | 32400 | A-           |
| 19    | 36100 | A            |
| 20    | 40000 | A+           |

While on the one hand this might sound a bit gimmicky, it's actually a really powerful re-framing of the concepts of assessment and evaluation in a course. This framing also makes assessment more authentic, in the sense that you are receiving credit for achieving specific, meaningful learning outcomes. It also recognizes that throughout the course, you are continuously building knowledge, experience, and skills.

The XP system is also built to be inclusive and adaptive to the need and life circumstances of individual students. While some assessments are not accepted after the due date, and some evaluations have late penalties, we recognize that missed or late assignments sometimes happen for excusable reasons. Rather than making a big deal about your proving to us that your reason is legitimate, we instead provide options for you to make up lost points in other ways. This also allows you to compensate for getting a lower grade on an assessment(s) than desired.

Because there are a variety of bonus points on offer, there are actually more opportunities to earn XP than you need to get an A+ in the course. This means that you can, within reason, pick and choose how to achieve your desired grade.  All that said, XP (and your grade) are intended to reflect the degree to which you have met the learning objectives, so you do need to demonstrate competence with regard to all of the objectives.

## How to Earn XP
The table below lists all the "core" and "bonus" opportunities to earn course XP.

| **Summative Evaluations (graded)**    | XP   | Bonus XP | Notes                      |
|---------------------------------------|------|----------|----------------------------|
| *Assignments*                         |      |          |                            |
| Assignment 1                          | 700  |          |                            |
| Assignments 2-6, 2nd best             | 3000 |          |                            |
| Assignments 2-6, 3rd best             | 3000 |          |                            |
| Assignments 2-6, 4th best             | 3000 |          |                            |
| Assignments 2-6, 5th best             |      | 1000     |                            |
| Assignments 2-6, 6th best             |      | 1000     |                            |
| *Projects*                            |      |          |                            |
| Project 1                             | 6000 |          |                            |
| Project 2                             | 8000 |          |                            |
| *Portfolio*                           |      |          |                            |
| Portfolio submission 1                | 1000 |          |                            |
| Portfolio submission 2                | 3000 |          |                            |
| *Demos*                               |      |          |                            |
| Demo 1                                | 1500 |          |                            |
| Demo 2                                | 1500 |          |                            |
| Demo 3                                | 1500 |          |                            |
| Demo 4                                |      | 500      |                            |
| Demo 5                                |      | 500      |                            |
| Demo 6                                |      | 500      |                            |
| Demo 7                                |      | 500      |                            |
| **Formative Assessments (Pass/Fail)** |      |          |                            |
| *Datacamp lessons*                    | 5000 |          | (DataCamp XP/10; max 5000) |
| *Peer Assessments*                    |      |          |                            |
| Demos: 1st peer assessment            | 100  |          |                            |
| Demos: 2nd peer assessment            | 100  |          |                            |
| Demos: 3rd peer assessment            | 100  |          |                            |
| Demos: 4th peer assessment            | 100  |          |                            |
| Demos: 5th peer assessment            | 100  |          |                            |
| Demos: 6th peer assessment            | 100  |          |                            |
| Project 1 peer assessment             | 500  |          |                            |
| Project 2 peer asessment              | 500  |          |                            |
| Complete all Peer Assessments         |      | 400      |                            |
| *Self-Assessments*                    |      |          |                            |
| Self-assessment 1                     | 150  |          |                            |
| Self-assessment 2                     | 150  |          |                            |
| Self-assessment 3                     | 150  |          |                            |
| Self-assessment 4                     | 150  |          |                            |
| Self-assessment 5                     | 150  |          |                            |
| Self-assessment 6                     | 150  |          |                            |
| Complete all self-assessments         |      | 400      |                            |
| *Meet 'n Greets*                      |      |          |                            |
| Slack snack or donut 1                | 100  |          |                            |
| Slack snack or donut 2                | 100  |          |                            |
| Slack snack or donut 3                | 100  |          |                            |
| Slack snack or donut 4                |      | 100      |                            |
| Slack snack or donut 5                |      | 100      |                            |
| Slack snack or donut 6                |      | 100      |                            |
| *Other Bonus Points*                  |      |          |                            |
| Did not ask for extension bonus       |      | 200      |                            |
| Project 1 team size > 3 people        |      | 200      |                            |
| Project 2 team size > 3 people        |      | 200      |                            |
| Typo reports                          |      | 250      | 50 ea, 5 max               |
| Add glossary entry                    |      | 400      | 100 ea, 4 max              |
| Glossary review                       |      | 200      | 50 ea, 4 max               |
| **Totals**                            | **40000** | **6150**     |                            |


That's a lot of ways to earn points! The table below summarizes how the points add up:

|                                      | XP    | % of A+ Grade |
|--------------------------------------|-------|---------------|
| Graded (summative evaluation) total  | 32200 | 80.5%         |
| Pass/Fail (formative assessment)     | 7800  | 19.5%         |
| Bonus graded total                   | 4000  | 10.0%         |
| Bonus P/F total                      | 2150  | 5.4%          |

# Schedule

(Very much subject to change prior to start of term!)

| Week | Class | Date       | Class topic                  | Lesson                                      | Summative Evaluations | Formative Assessments |
|------|-------|------------|------------------------------|---------------------------------------------|-----------------------|-----------------------|
| 0    | 0     | pre-course |                              | Online textbook, chapter 1                  |                       |                       |
| 1    | 1     | July 06    | Live introductions           |                                             |                       |                       |
|      | 2     | July 07    |                              | Online textbook, ch. 2                      | Assignment 1          |                       |
|      | 3     | July 08    | check-in                     | Introduction to Python                      |                       | self-assessment 1     |
|      | 4     | July 09    |                              |                                             |                       |                       |
|      | 5     | July 10    | demo day                     | Intermediate Python                         | Demo                  |                       |
| 2    | 6     | July 13    |                              | Pandas Foundations                          | Assignment 2          |                       |
|      | 7     | July 14    |                              |                                             |                       |                       |
|      | 8     | July 15    | check-in                     | Manipulating DataFrames with pandas         |                       | self-assessment 2     |
|      | 9     | July 16    |                              |                                             |                       |                       |
|      | 10    | July 17    | demo day                     |                                             | Demo                  |                       |
| 3    | 11    | July 20    |                              | Merging DataFrames with pandas              | Assignment 3          |                       |
|      | 12    | July 21    |                              |                                             |                       |                       |
|      | 13    | July 22    | check-in                     | Intro to Data Visualization with Matplotlib |                       | self-assessment 3     |
|      | 14    | July 23    |                              |                                             |                       |                       |
|      | 15    | July 24    | demo day                     | Intro to Data Visualization with Seaborn    | Demo                  |                       |
| 4    | 16    | July 27    | Introducing single unit data | Statistical Thinking in Python              | Project 1             |                       |
|      | 17    | July 28    |                              |                                             |                       |                       |
|      | 18    | July 29    | check-in                     |                                             |                       | peer assessment 3     |
|      | 19    | July 30    |                              |                                             |                       |                       |
|      | 20    | July 31    | demo day                     |                                             | Demo                  |                       |
| 5    |       |            | Long Weekend!!!              |                                             |                       |                       |
|      | 21    | August 04  | Introducing EEG data         |                                             | Assignment 4          |                       |
|      | 22    | August 05  | check-in                     |                                             |                       | self-assessment 4     |
|      | 23    | August 06  |                              |                                             |                       |                       |
|      | 24    | August 07  | demo day                     |                                             | Demo                  |                       |
| 6    | 25    | August 10  | Working with MRI data        | Biomedical Image Analysis with Python       | Assignment 5          |                       |
|      | 26    | August 11  |                              |                                             |                       |                       |
|      | 27    | August 12  | check-in                     |                                             |                       | self-assessment 5     |
|      | 28    | August 13  |                              |                                             |                       |                       |
|      | 29    | August 14  | demo day                     |                                             | Demo                  |                       |
| 7    | 30    | August 17  | project check-in             | Machine Learning for Everyone               | Assignment 6          |                       |
|      | 31    | August 18  |                              |                                             |                       |                       |
|      | 32    | August 19  | check-in                     |                                             |                       | self-assessment 6     |
|      | 33    | August 20  |                              |                                             |                       |                       |
|      | 34    | August 21  | check-in                     |                                             | Demo                  |                       |
| 8    | 35    | August 24  | demo day                     |                                             | Project 2             | peer assessment       |


# Policies
This course is governed by the academic rules and regulations set forth in the University Calendar and by Senate.

## Attendance
Attendance scheduled class meetings is optional. However, due to the flipped classroom model, scheduled class times are the only time when you can ask the instructor for help or guidance with coursework. You may also find some of the discussions held during class time useful to support your learning. Outside of scheduled class time, the instructor is not available to help with course work. However, if you have other issues you need to discuss (e.g., personal reasons that make it difficult for you to succeed in the class), you may contact the instructor by email to discuss the matter either that way, or in a meeting (online or in-person).

## Academic Freedom
Freedom of speech and of thought are cornerstones of academic institutions such as Dalhousie. Our goal in science is to observe and characterize the world accurately and objectively. However, we must realize that our perceptions of reality are often coloured by our beliefs and assumptions, some of which we may not be aware of. Academic freedom includes not only the freedom to think as you please, but others’ freedom do express their beliefs as well. Please do not hesitate to express your ideas, but do so in a way that is respectful of others. This is the only avenue for the free expression and exchange of ideas.

## Academic Integrity
At Dalhousie University, we are guided in all of our work by the values of academic integrity: honesty, trust, fairness, responsibility and respect (The Center for Academic Integrity, Duke University, 1999). As a student, you are required to demonstrate these values in all of the work you do. The University provides policies and procedures that every member of the university community is required to follow to ensure academic integrity. For more details please see: [https://www.dal.ca/dept/university\_secretariat/academic-integrity.html](https://www.dal.ca/dept/university\_secretariat/academic-integrity.html)  

## Accessibility
The Advising and Access Services Centre is Dalhousie's centre of expertise for student accessibility and accommodation. The advising team works with students who request accommodation as a result of a disability, religious obligation, or any barrier related to any other characteristic protected under Human Rights legislation (Canada and Nova Scotia).
Information: [https://www.dal.ca/campus\_life/academic-support/accessibility.html](https://www.dal.ca/campus\_life/academic-support/accessibility.html)

## Code of Student Conduct
Everyone at Dalhousie is expected to treat others with dignity and respect. The Code of Student Conduct allows Dalhousie to take disciplinary action if students don’t follow this community expectation. When appropriate, violations of the code can be resolved in a reasonable and informal manner—perhaps through a restorative justice process. If an informal resolution can’t be reached, or would be inappropriate, procedures exist for formal dispute resolution. For more information please see [https://www.dal.ca/campus\_life/safety-respect/student-rights-and-responsibilities/student-lifepolicies/code-of-student-conduct.html](https://www.dal.ca/campus\_life/safety-respect/student-rights-and-responsibilities/student-lifepolicies/code-of-student-conduct.html)

## Important Dates in the Academic Year (including add/drop dates)
[https://www.dal.ca/academics/important\_dates.html](https://www.dal.ca/academics/important\_dates.html)

## University Grading Practices
[https://www.dal.ca/dept/university\_secretariat/policies/academic/grading-practices-policy.html](https://www.dal.ca/dept/university\_secretariat/policies/academic/grading-practices-policy.html)

## Missed or Late Academic Requirements due to Student Absence (policy)
[https://www.dal.ca/dept/university\_secretariat/policies/academic/missed-or-late-academicrequirements-due-to-student-absence.html
](https://www.dal.ca/dept/university\_secretariat/policies/academic/missed-or-late-academicrequirements-due-to-student-absence.html
)
## Learning and Support Resources

### Advising
General Advising [https://www.dal.ca/campus\_life/academic-support/advising.html](https://www.dal.ca/campus\_life/academic-support/advising.html)

Science Program Advisors: [https://www.dal.ca/faculty/science/current-students/academic-advising.html](https://www.dal.ca/faculty/science/current-students/academic-advising.html)

Indigenous Student Centre: [https://www.dal.ca/campus\_life/communities/indigenous.html](https://www.dal.ca/campus\_life/communities/indigenous.html  )

Black Students Advising Centre: [https://www.dal.ca/campus\_life/communities/black-student-advising.html](https://www.dal.ca/campus\_life/communities/black-student-advising.html)

International Centre: [https://www.dal.ca/campus\_life/international-centre/current-students.html](https://www.dal.ca/campus\_life/international-centre/current-students.html)

### Academic supports
Library: [https://libraries.dal.ca](https://libraries.dal.ca)  

Writing Centre: [https://www.dal.ca/campus\_life/academic-support/writing-and-study-skills.html](https://www.dal.ca/campus\_life/academic-support/writing-and-study-skills.html)

Studying for Success: [https://www.dal.ca/campus\_life/academic-support/study-skills-and-tutoring.html](https://www.dal.ca/campus\_life/academic-support/study-skills-and-tutoring.html)

Copyright Office: [https://libraries.dal.ca/services/copyright-office.html](https://libraries.dal.ca/services/copyright-office.html)  

Fair Dealing Guidelines [https://libraries.dal.ca/services/copyright-office/fair-dealing.html](https://libraries.dal.ca/services/copyright-office/fair-dealing.html)

### Other supports and services
Student Health & Wellness Centre: [https://www.dal.ca/campus\_life/health-and-wellness/servicessupport/student-health-and-wellness.html](https://www.dal.ca/campus\_life/health-and-wellness/servicessupport/student-health-and-wellness.html)

Student Advocacy: [https://dsu.ca/dsas](https://dsu.ca/dsas)

Ombudsperson: [https://www.dal.ca/campus\_life/safety-respect/student-rights-and-responsibilities/where-to-get-help/ombudsperson.html](https://www.dal.ca/campus\_life/safety-respect/student-rights-and-responsibilities/where-to-get-help/ombudsperson.html)

### Safety

Biosafety: [https://www.dal.ca/dept/safety/programs-services/biosafety.html](https://www.dal.ca/dept/safety/programs-services/biosafety.html)

Chemical Safety: [https://www.dal.ca/dept/safety/programs-services/chemical-safety.html](https://www.dal.ca/dept/safety/programs-services/chemical-safety.html)

Radiation Safety: [https://www.dal.ca/dept/safety/programs-services/radiation-safety.html](https://www.dal.ca/dept/safety/programs-services/radiation-safety.html)

Scent-Free Program: [https://www.dal.ca/dept/safety/programs-services/occupational-safety/scent-free.html](https://www.dal.ca/dept/safety/programs-services/occupational-safety/scent-free.html)
