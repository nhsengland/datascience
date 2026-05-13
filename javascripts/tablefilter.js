function tableFilter(table_id, input_id) {
  // Declare variables
  var input, filter, table, tr, td, i, txtValue;
  input = document.getElementById(input_id);
  filter = input.value.toUpperCase();
  table = document.getElementById(table_id);
  tr = table.getElementsByTagName("tr");
  const columnSelector = document.getElementById("columnToSearch").value;
  
  console.log(columnSelector)
  // Loop through all table rows, and hide those who don't match the search query
  const columnNames = ['Name','Role', 'Team', 'Github']
  const columnIndex = columnNames.indexOf(columnSelector)

  for (i=0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[columnIndex];
    if (td) {
      txtValue = td.textContent || td.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}