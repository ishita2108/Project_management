
  function didRedirect(){
    window.location.href='/'
  }

  // Delete Student Script
  function handleStuDelete(e){
    e.preventDefault()
    console.log(stuDelEl.value)
    const myForm = stuDelEl
    console.log(myForm)
    const myFormData = new FormData(myForm)
    console.log(myFormData)
    const url = '/delete-student'
    const method = "POST"
    const xhr = new XMLHttpRequest()
    const responseType ="json"
    xhr.responseType = responseType
    xhr.open(method,url)
    xhr.setRequestHeader("HTTP_X_REQUESTED_WITH", "XMLHttpRequest") //In order to make django return "true" when queried request.is_ajax()
    xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest")
    xhr.onload = function(){
    //console.log(xhr.response) log the response thats coming back
    if(xhr.status === 200) {
        console.log(xhr.response)
        // const newStudentJson = xhr.response //response will give tweet element in json
        didRedirect()
        //const newTweetJson = JSON.parse(newTweet)
        //console.log(newTweetJson.likes)
        

        }
  }
  xhr.onerror = function(){
    alert('ERROR!');
  }
  xhr.send(myFormData)
  }

  const stuDelEl = document.getElementById('stu-delete-form')
  stuDelEl.addEventListener("submit",handleStuDelete)

// Edit Student Script

  function didUpdate(id){
    console.log(id)
    window.location.href=`/student/${id}`
  }

  function handleStuEdit(e){
    console.log('Edit Submit')
    e.preventDefault()
    const myForm = stuEditEl
    console.log(myForm)
    const myFormData = new FormData(myForm)
    console.log(myFormData)
    const url = '/edit-student'
    const method = "POST"
    const xhr = new XMLHttpRequest()
    const responseType ="json"
    xhr.responseType = responseType
    xhr.open(method,url)
    xhr.setRequestHeader("HTTP_X_REQUESTED_WITH", "XMLHttpRequest") //In order to make django return "true" when queried request.is_ajax()
    xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest")
    xhr.onload = function(){
    //console.log(xhr.response) log the response thats coming back
    if(xhr.status === 201) {
        
        console.log(xhr.response)
        stu_id = xhr.response.msg
        didUpdate(stu_id)

        }
   }
  xhr.onerror = function(){
  alert('ERROR!');
  }
   xhr.send(myFormData)
  }


  const stuEditEl = document.getElementById('stu-edit-form')
  stuEditEl.addEventListener("submit",handleStuEdit)
  
  
    