---
layout: post
status: publish
published: true
title: FileZilla - Easily edit files on a remote server with your favorite local editor
author:
  display_name: mvukas
  login: mvukas
  email: mattvukas@gmail.com
  url: ''
author_login: mvukas
author_email: mattvukas@gmail.com
wordpress_id: 363
wordpress_url: http://mattvukas.com/?p=363
date: '2014-01-18 14:21:05 -0700'
date_gmt: '2014-01-18 19:21:05 -0700'
---
<p>FileZilla is a great free and open source FTP client. As far as standalone FTP clients go, I'd be willing to bet that it's the most widely used client of it's type. Without the data to back that up, I'd only assume it based on how many times I've seen it used by universities, companies, and freelance developers.</p>
<p>While being relatively straightforward, FileZilla is pretty feature rich, even including the ability to edit files remotely using your favorite local, GUI text editor. That's what I'll show in this article.</p>
<p><a id="more"></a><a id="more-363"></a></p>
<p>This tutorial is done in Windows 8 64bit, but should be very similar on any OS. To enable this feature, click "Edit" in the toolbar then go to "Settings". On the left column of the options window, select "File editing":</p>
<p><a href="http://mattvukas.com/wp-content/uploads/2014/01/cap2.png"><img class="aligncenter size-full wp-image-366" alt="cap2" src="http://mattvukas.com/wp-content/uploads/2014/01/cap2.png" width="607" height="392" /></a></p>
<p>Then select "Use custom editor:", followed by selecting the program you want to use below. Finally, to make sure Windows always opens these server files up in a text editor, select the "Always use default editor" radio button. "Watch locally edited file and prompt to upload modifications" should already be checked, but make sure to check it if you want to enable that feature.</p>
<p>That's it! Now when you right click a file on the server and click "View/edit", you will be able to edit a temporary local copy on your computer. After you save the file and refocus on the FileZilla window, FileZilla will ask you if you want to upload the changes you made, which it detected. How cool is that?</p>
