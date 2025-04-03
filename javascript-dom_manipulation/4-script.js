document.getElementById('add_item').addEventListener('click', myfunction);
function myfunction() {
    const node = document.createElement('li');
    const textnode = document.createTextNode('Item');
    node.appendChild(textnode);
    document.querySelector('.my_list').appendChild(node);
}
