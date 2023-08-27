<!doctype html>
<html>
 <head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
  <title>Karl Johnson - Home</title>
  <link rel="shortcut icon" type="image/png" href="format_images/title_icon.png" />
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Julius+Sans+One">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat:100,200,400">
  <link rel="stylesheet" href="style.css"> 
  <style type="text/css">
    #wide-menu-item {
        height: 150px;
        width: 100%;
        position: relative;
        margin: 0px;
        padding: 0px;
        border: 0px;
        font-size: 0px;
        display: inline-block;
        overflow: hidden;
        
    }
    
    #wide-menu-item img {
        height: 150px;
        width: 100%;
        top: 50%;
        left: 50%;
        margin: 0px;
        padding: 0px;
        border: 0px;
        object-fit: cover;
        overflow: hidden;
        outline: none;
        filter: blur(10px);
        transform: scale(1.2);
    }
    
    #wide-menu-item span {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        color: white;
        font-family: "Julius Sans One";
        font-size: 30px;
        text-align: center;
        margin: 0px;
        padding: 0px;
        border: 0px;
    }
    #wide-menu-item:hover img {
        filter: blur(10px) brightness(.3);
        
    }
    #wide-menu-item:hover span {
        font-size: 30px;
    }
    #panorama {
        width: 90%; /* fallback */
        width: calc(100% - 50px);
        height: 300px;
        /* margin-top: 50px; */
        margin-left: 50px;
    }
  </style>
 </head>
 <body>
  <?php include($_SERVER['DOCUMENT_ROOT'].'/sidebar.html'); ?>
  <script src="/openseadragon/openseadragon.js"></script>
  <div id="content">
   <t1> welcome </t1><br>
   <p> I mainly use this website to show off my panoramas and personal engineering projects, though I sometimes post interesting things I've done for work and school. </p>
  </div>
  
  <div id="grid">
   <a href="projects/20201201-panoramic-head">
    <span id="wide-menu-item">
     <img src="projects/20201201_thumb.jpg">
     <span>Featured: Motorized Panoramic Tripod Head!</span>
    </span>
   </a>
   <a href="photos/Panoramas/">
    <span id="wide-menu-item">
     <img src="pano_background.jpg">
     <span> go to panoramas</span>
    </span>
   </a>
   <a href="projects/">
    <span id="wide-menu-item">
     <img src="coming-soon/28-135_thumb.jpg">
     <span> go to projects</span>
    </span>
   </a>
  </div>
  <!--<div id="panorama"></div>
  <script type="text/javascript">
		var viewer = OpenSeadragon({
		id: "panorama",
		prefixUrl: "/openseadragon/images/",
		tileSources: "photos/Panoramas/20210327/20210327_1022/20210327_1022.dzi",
		showNavigator:  true
		});
		viewer.bookmarkUrl();
	</script>-->
  <?php include($_SERVER['DOCUMENT_ROOT'].'/footer.html'); ?>
 </body>
</html> 
