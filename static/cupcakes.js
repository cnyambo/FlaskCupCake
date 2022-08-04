 
async function add_dessert(e){
    e.preventDefault();
    try{
        const resp = await axios.post(`http://127.0.0.1:5000/api/cupcakes`, 
        {flavor:flavor, size:size, rating:rate, image:img})  
        console.log(resp.data)

    }catch(error){
        console.log(error)
    }
};
