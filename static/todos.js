$('.delete-todo').click(delete_todo)

async function delete_todo(){
   const id= $(this).data('id')
    await axios.delete(`/api/todos/${id}`)
    $(this).parent.remove()
}