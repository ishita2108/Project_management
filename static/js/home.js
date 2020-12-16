function handleStuCreateFormDidSubmit(event){
    event.preventDefault()
    const myForm = event.target
    console.log(myForm)
    const myFormData = new FormData(myForm)
    console.log(myFormData)
    const url = myForm.getAttribute("action")
    const method = myForm.getAttribute("method")
    const xhr = new XMLHttpRequest()
    const responseType ="json"
    xhr.responseType = responseType
    xhr.open(method,url)
    xhr.setRequestHeader("HTTP_X_REQUESTED_WITH", "XMLHttpRequest") //In order to make django return "true" when queried request.is_ajax()
    xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest")
    xhr.onload = function(){
    //console.log(xhr.response) log the response thats coming back
    if(xhr.status === 201) {
        //handleTweetFormError("Success", false)
        console.log(xhr.response)
        const newStudentJson = xhr.response //response will give tweet element in json
        //const newTweetJson = JSON.parse(newTweet)
        //console.log(newTweetJson.likes)
        const newStudentElement = formatStudentTableEl(newStudentJson)
        const ogHtml = tableConEl.innerHTML
        tableConEl.innerHTML = newStudentElement + ogHtml
        myForm.reset() // to clear the previous tweet after successfully tweeting

        }
    if(xhr.status === 400){
      console.log(xhr.response)
      alert(xhr.response.msg)
    }
  }
  xhr.onerror = function(){
    alert('ERROR!');
  }
  xhr.send(myFormData)
  }

  const formatStudentTableEl = (props) => {
    const student = props
    const formattedStu = "<tr><th scope='row'>#</th><td>"+ student.name +"</td><td>"+student.project.name+"</td><td>"+student.project.language+"</td><td> " + student.section +"</td></tr>"
    return formattedStu
  }

  const stuCreateFormEl = document.getElementById('stu-create-form')
  const tableConEl = document.getElementById('table-body')
  stuCreateFormEl.addEventListener("submit",handleStuCreateFormDidSubmit)

  
    