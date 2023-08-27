<!doctype html>
<html>
 <head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
  <title>Karl Johnson - HEADER TITLE</title>
  <link rel="shortcut icon" type="image/png" href="format_images/title_icon.png" />
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Julius+Sans+One">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat:100,200,400">
  <link rel="stylesheet" href="style.css"> 
 </head>
 <body>
  <?php include($_SERVER['DOCUMENT_ROOT'].'/sidebar.html'); ?>
  <div id="content">
   <t1> TITLE TEXT </t1><br>
   <p> BODY TEXT</p>
  </div>
  <div id="grid">
   <a href="BIG_LINK_PATH">
    <span id="banner-thumbnail">
     <img src="BIG_LINK_THUMBNAIL">
     <span> DISPLAYED TEXT</span>
    </span>
   </a>
   <a href="SMALL_LINK_PATH">
    <span id="thumbnail">
     <img src="SMALL_LINK_THUMBNAIL">
     <span> DISPLAYED TEXT</span>
    </span>
   </a>
  </div> 
  <?php include($_SERVER['DOCUMENT_ROOT'].'/footer.html'); ?>
 </body>
</html> 
