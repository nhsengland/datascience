document$.subscribe(function() {
    var tables = document.querySelectorAll("article table:not([class])")
    tables.forEach(function(table) {
      var tf = new TableFilter(table)  
      tf.init()
    })  
  })