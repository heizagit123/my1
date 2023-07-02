  <script>
                            let department_courses = [
                            {
                                department: "Computer Science",
                                code:"cs",
                                courses:["BSc","MSc"]
                            },
                            {
                                department: "Commerce",
                                code:"commerce",
                                course:["BCom","MCom"]

                            },
                            {
                                department: "Politics",
                                code:"politics",
                                course:["BA","MA"]
                            },
                            {
                                department: "Zoology",
                                code:"zoology",
                                course:["BSc","MSc"]
                            },
                            {
                                department: "Psychology",
                                code:"psychology",
                                course:["BA","MA"]
                            }
                    ]


                        let departmentselect = document.querySelector('#departments');
                        let courseselect = document.querySelector('#courses');


                        departmentselect.onchange = function()
                        {

                            courseselect.options =null;
                            if(departmentselect.value!=-1){
                                for(ele of department_courses){
                                    if(departmentselect.value == ele.code){

                                        let courses = ele.courses;
                                        let op= document.createElement('option');
                                        op.value =-1;
                                        op.innerText ="Select Course";
                                        courseselect.options[0] = op;
                                        let i=1;

                                        for(course of courses){

                                            let op= document.createElement('option';
                                            op.value =courses;
                                            op.innerText ="course";
                                            courseselect.options[i] = op;
                                            i++;
                                        }

                                        }
                                    }

                                }



                            }
                        }
                    </script>
