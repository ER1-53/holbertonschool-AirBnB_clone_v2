# AirBnB clone - Web framework

<a href="https://intranet.hbtn.io/concepts/865" title="Concepts" target="_blank">Concepts</a>


<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/qk3bO45DSY-P4qmdnEX93w" title="What is a Web Framework?" target="_blank">What is a Web Framework?</a> </li>
<li><a href="/rltoken/DCF-0NHTuXLykc1ijX5HVg" title="A Minimal Application" target="_blank">A Minimal Application</a> </li>
<li><a href="/rltoken/mfdHqOmCsS7veXQ3nK6PcQ" title="Routing" target="_blank">Routing</a> (<em>except &ldquo;HTTP Methods&rdquo;</em>)</li>
<li><a href="/rltoken/_dU2691FhIZB3lBtSF5nMg" title="Rendering Templates" target="_blank">Rendering Templates</a> </li>
<li><a href="/rltoken/V24BEPWuJb3yPZpOvA3-Zw" title="Synopsis" target="_blank">Synopsis</a> </li>
<li><a href="/rltoken/GKvdWdthYkstOwnDs9LJWg" title="Variables" target="_blank">Variables</a> </li>
<li><a href="/rltoken/qum7hVpPWLaqMZBQCpcRyA" title="Comments" target="_blank">Comments</a> </li>
<li><a href="/rltoken/LxOb-5Fe9bHvx0TguTDY9g" title="Whitespace Control" target="_blank">Whitespace Control</a> </li>
<li><a href="/rltoken/8D9OoDX5cYQOFXUqwAiCNw" title="List of Control Structures" target="_blank">List of Control Structures</a> (<em>read up to &ldquo;Call&rdquo;</em>)</li>
<li><a href="/rltoken/OMqE9vlalgkWcT_3fu4Hvg" title="Flask" target="_blank">Flask</a> </li>
<li><a href="/rltoken/L3kYnmfrbc86Asb4JZq0rg" title="Jinja" target="_blank">Jinja</a> </li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/lVg3jl6IEzhNeQiHwhC-Fg" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What is a Web Framework</li>
<li>How to build a web framework with Flask</li>
<li>How to define routes in Flask</li>
<li>What is a route</li>
<li>How to handle variables in a route</li>
<li>What is a template</li>
<li>How to create a HTML response in Flask by using a template</li>
<li>How to create a dynamic template (loops, conditions&hellip;)</li>
<li>How to display in HTML data from a MySQL database</li>
</ul>

<h2>Requirements</h2>

<h3>Python Scripts</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the pycodestyle (version 2.7.*)</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
<li>All your modules should have documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).__doc__)&#39;</code>)</li>
<li>All your classes should have documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.__doc__)&#39;</code>)</li>
<li>All your functions (inside and outside a class) should have documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).my_function.__doc__)&#39;</code> and <code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.my_function.__doc__)&#39;</code>)</li>
<li>A documentation is not a simple word, it&rsquo;s a real sentence explaining what&rsquo;s the purpose of the module, class or method (the length of it will be verified)</li>
</ul>

<h3>HTML/CSS Files</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files should end with a new line</li>
<li>A <code>README.md</code> file at the root of the folder of the project is mandatory</li>
<li>Your code should be W3C compliant and validate with <a href="/rltoken/BABHSFrobycuS0xRtRtXVQ" title="W3C-Validator" target="_blank">W3C-Validator</a> (except for jinja template)</li>
<li>All your CSS files should be in the <code>styles</code> folder</li>
<li>All your images should be in the <code>images</code> folder</li>
<li>You are not allowed to use <code>!important</code> or <code>id</code> (<code>#...</code> in the CSS file)</li>
<li>All tags must be in uppercase</li>
<li>Current screenshots have been done on <code>Chrome 56.0.2924.87</code>. </li>
<li>No cross browsers </li>
</ul>

<h2>More Info</h2>

<h3>MySQL Default charset issues</h3>

<ul>
<li>If you get Flask errors after executing the  <code>curl ...</code> commands, it might be because of the <code>DEFAULT CHARSET</code>. If it&rsquo;s <code>DEFAULT CHARSET=latam1</code>, you might want to change it to <code>DEFAULT CHARSET=utf8mb4</code>, either on the server&rsquo;s config file (/etc/mysql/my.cnf commonly) orm on the CREATE DATABASE statement.</li>
</ul>

<h3>Install Flask</h3>

<pre><code>$ pip3 install Flask
</code></pre>

<p><img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/concepts/74/hbnb_step3.png" alt="" loading='lazy' style="" /></p>

<iframe width="560" height="315" src="https://www.youtube.com/embed/lzs4nQOiZQY" frameborder="0" allowfullscreen></iframe>

<h3>NOTE:</h3>

<ul>
<li>Try setting FLASK configuration <code>debug</code> to <code>False</code>  iIf you get the following error when running the checker:</li>
</ul>

<pre><code> - [Got]
rpc error: code = 2 desc = oci runtime error: exec failed: container_linux.go:290: starting container process caused &quot;process_linux.go:111: decoding init error from pipe caused \&quot;read parent: connection reset by peer\&quot;&quot;


(222 chars long)
</code></pre>

<h3>Manual QA Review</h3>

<p><strong>It is your responsibility to request a review for this project from a peer before the project’s deadline. If no peers have been reviewed, you should request a review from a TA or staff member.</strong></p>


<details>
<summary>Click to see: Tasks</summary>

<h3 class="panel-title">
0. Hello Flask!
</h3>

Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>Routes:

<ul>
<li><code>/</code>: display &ldquo;Hello HBNB!&rdquo;</li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>

<pre><code>guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.0-hello_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In another tab:</p>

<pre><code>guillaume@ubuntu:~$ curl 0.0.0.0:5000 ; echo &quot;&quot; | cat -e
Hello HBNB!$
guillaume@ubuntu:~$ 
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-AirBnB_clone_v2</code></li>
<li>Directory: <code>web_flask</code></li>
<li>File: <code>0-hello_route.py, __init__.py</code></li>
</ul>
</div>

<h3 class="panel-title">
1. HBNB
</h3>

Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>Routes:

<ul>
<li><code>/</code>: display &ldquo;Hello HBNB!&rdquo;</li>
<li><code>/hbnb</code>: display &ldquo;HBNB&rdquo;</li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>

<pre><code>guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.1-hbnb_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In another tab:</p>

<pre><code>guillaume@ubuntu:~$ curl 0.0.0.0:5000/hbnb ; echo &quot;&quot; | cat -e
HBNB$
guillaume@ubuntu:~$ 
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-AirBnB_clone_v2</code></li>
<li>Directory: <code>web_flask</code></li>
<li>File: <code>1-hbnb_route.py</code></li>
</ul>
</div>

<h3 class="panel-title">
2. C is fun!
</h3>

Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>Routes:

<ul>
<li><code>/</code>: display &ldquo;Hello HBNB!&rdquo;</li>
<li><code>/hbnb</code>: display &ldquo;HBNB&rdquo;</li>
<li><code>/c/&lt;text&gt;</code>: display &ldquo;C &rdquo; followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)</li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>

<pre><code>guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.2-c_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In another tab:</p>

<pre><code>guillaume@ubuntu:~$ curl 0.0.0.0:5000/c/is_fun ; echo &quot;&quot; | cat -e
C is fun$
guillaume@ubuntu:~$ curl 0.0.0.0:5000/c/cool ; echo &quot;&quot; | cat -e
C cool$
guillaume@ubuntu:~$ curl 0.0.0.0:5000/c
&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 3.2 Final//EN&quot;&gt;
&lt;title&gt;404 Not Found&lt;/title&gt;
&lt;h1&gt;Not Found&lt;/h1&gt;
&lt;p&gt;The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.&lt;/p&gt;
guillaume@ubuntu:~$ 
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-AirBnB_clone_v2</code></li>
<li>Directory: <code>web_flask</code></li>
<li>File: <code>2-c_route.py</code></li>
</ul>
</div>

<h3 class="panel-title">
3. Python is cool!
</h3>

Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>Routes:

<ul>
<li><code>/</code>: display &ldquo;Hello HBNB!&rdquo;</li>
<li><code>/hbnb</code>: display &ldquo;HBNB&rdquo;</li>
<li><code>/c/&lt;text&gt;</code>: display &ldquo;C &rdquo;, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)</li>
<li><code>/python/&lt;text&gt;</code>: display &ldquo;Python &rdquo;, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)

<ul>
<li>The default value of <code>text</code> is &ldquo;is cool&rdquo;</li>
</ul></li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>

<pre><code>guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.3-python_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In another tab:</p>

<pre><code>guillaume@ubuntu:~$ curl -Ls 0.0.0.0:5000/python/is_magic ; echo &quot;&quot; | cat -e
Python is magic$
guillaume@ubuntu:~$ curl -Ls 0.0.0.0:5000/python ; echo &quot;&quot; | cat -e
Python is cool$
guillaume@ubuntu:~$ curl -Ls 0.0.0.0:5000/python/ ; echo &quot;&quot; | cat -e
Python is cool$
guillaume@ubuntu:~$ 
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-AirBnB_clone_v2</code></li>
<li>Directory: <code>web_flask</code></li>
<li>File: <code>3-python_route.py</code></li>
</ul>
</div>

<h3 class="panel-title">
4. Is it a number?
</h3>

Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>Routes:

<ul>
<li><code>/</code>: display &ldquo;Hello HBNB!&rdquo;</li>
<li><code>/hbnb</code>: display &ldquo;HBNB&rdquo;</li>
<li><code>/c/&lt;text&gt;</code>: display &ldquo;C &rdquo;, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)</li>
<li><code>/python/&lt;text&gt;</code>: display &ldquo;Python &rdquo;, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)

<ul>
<li>The default value of <code>text</code> is &ldquo;is cool&rdquo;</li>
</ul></li>
<li><code>/number/&lt;n&gt;</code>: display &ldquo;<code>n</code> is a number&rdquo; <strong>only</strong> if <code>n</code> is an integer</li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>

<pre><code>guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.4-number_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In another tab:</p>

<pre><code>guillaume@ubuntu:~$ curl 0.0.0.0:5000/number/89 ; echo &quot;&quot; | cat -e
89 is a number$
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number/8.9 
&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 3.2 Final//EN&quot;&gt;
&lt;title&gt;404 Not Found&lt;/title&gt;
&lt;h1&gt;Not Found&lt;/h1&gt;
&lt;p&gt;The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.&lt;/p&gt;
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number/python 
&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 3.2 Final//EN&quot;&gt;
&lt;title&gt;404 Not Found&lt;/title&gt;
&lt;h1&gt;Not Found&lt;/h1&gt;
&lt;p&gt;The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.&lt;/p&gt;
guillaume@ubuntu:~$ 
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-AirBnB_clone_v2</code></li>
<li>Directory: <code>web_flask</code></li>
<li>File: <code>4-number_route.py</code></li>
</ul>
</div>

<h3 class="panel-title">
5. Number template
</h3>

Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>Routes:

<ul>
<li><code>/</code>: display &ldquo;Hello HBNB!&rdquo;</li>
<li><code>/hbnb</code>: display &ldquo;HBNB&rdquo;</li>
<li><code>/c/&lt;text&gt;</code>: display &ldquo;C &rdquo;, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)</li>
<li><code>/python/&lt;text&gt;</code>: display &ldquo;Python &rdquo;, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)

<ul>
<li>The default value of <code>text</code> is &ldquo;is cool&rdquo;</li>
</ul></li>
<li><code>/number/&lt;n&gt;</code>: display &ldquo;<code>n</code> is a number&rdquo; <strong>only</strong> if <code>n</code> is an integer</li>
<li><code>/number_template/&lt;n&gt;</code>: display a HTML page <strong>only</strong> if <code>n</code> is an integer: 

<ul>
<li><code>H1</code> tag: &ldquo;Number: <code>n</code>&rdquo; inside the tag <code>BODY</code> </li>
</ul></li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>

<pre><code>guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.5-number_template
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In another tab:</p>

<pre><code>guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_template/89 ; echo &quot;&quot;
&lt;!DOCTYPE html&gt;
&lt;HTML lang=&quot;en&quot;&gt;
&lt;HEAD&gt;
&lt;TITLE&gt;HBNB&lt;/TITLE&gt;
&lt;/HEAD&gt;
&lt;BODY&gt;
&lt;H1&gt;Number: 89&lt;/H1&gt;
&lt;/BODY&gt;
&lt;/HTML&gt;
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_template/8.9 
&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 3.2 Final//EN&quot;&gt;
&lt;title&gt;404 Not Found&lt;/title&gt;
&lt;h1&gt;Not Found&lt;/h1&gt;
&lt;p&gt;The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.&lt;/p&gt;
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_template/python 
&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 3.2 Final//EN&quot;&gt;
&lt;title&gt;404 Not Found&lt;/title&gt;
&lt;h1&gt;Not Found&lt;/h1&gt;
&lt;p&gt;The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.&lt;/p&gt;
guillaume@ubuntu:~$ 
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-AirBnB_clone_v2</code></li>
<li>Directory: <code>web_flask</code></li>
<li>File: <code>5-number_template.py, templates/5-number.html</code></li>
</ul>
</div>

<h3 class="panel-title">
6. Odd or even?
</h3>

Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>Routes:

<ul>
<li><code>/</code>: display &ldquo;Hello HBNB!&rdquo;</li>
<li><code>/hbnb</code>: display &ldquo;HBNB&rdquo;</li>
<li><code>/c/&lt;text&gt;</code>: display &ldquo;C &rdquo;, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)</li>
<li><code>/python/&lt;text&gt;</code>: display &ldquo;Python &rdquo;, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)

<ul>
<li>The default value of <code>text</code> is &ldquo;is cool&rdquo;</li>
</ul></li>
<li><code>/number/&lt;n&gt;</code>: display &ldquo;<code>n</code> is a number&rdquo; <strong>only</strong> if <code>n</code> is an integer</li>
<li><code>/number_template/&lt;n&gt;</code>: display a HTML page <strong>only</strong> if <code>n</code> is an integer: 

<ul>
<li><code>H1</code> tag: &ldquo;Number: <code>n</code>&rdquo; inside the tag <code>BODY</code></li>
</ul></li>
<li><code>/number_odd_or_even/&lt;n&gt;</code>: display a HTML page <strong>only</strong> if <code>n</code> is an integer: 

<ul>
<li><code>H1</code> tag: &ldquo;Number: <code>n</code> is <code>even|odd</code>&rdquo; inside the tag <code>BODY</code></li>
</ul></li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>

<pre><code>guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.6-number_odd_or_even
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In another tab:</p>

<pre><code>guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_odd_or_even/89 ; echo &quot;&quot;
&lt;!DOCTYPE html&gt;
&lt;HTML lang=&quot;en&quot;&gt;
&lt;HEAD&gt;
&lt;TITLE&gt;HBNB&lt;/TITLE&gt;
&lt;/HEAD&gt;
&lt;BODY&gt;
&lt;H1&gt;Number: 89 is odd&lt;/H1&gt;
&lt;/BODY&gt;
&lt;/HTML&gt;
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_odd_or_even/32 ; echo &quot;&quot;
&lt;!DOCTYPE html&gt;
&lt;HTML lang=&quot;en&quot;&gt;
&lt;HEAD&gt;
&lt;TITLE&gt;HBNB&lt;/TITLE&gt;
&lt;/HEAD&gt;
&lt;BODY&gt;
&lt;H1&gt;Number: 32 is even&lt;/H1&gt;
&lt;/BODY&gt;
&lt;/HTML&gt;
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_odd_or_even/python 
&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 3.2 Final//EN&quot;&gt;
&lt;title&gt;404 Not Found&lt;/title&gt;
&lt;h1&gt;Not Found&lt;/h1&gt;
&lt;p&gt;The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.&lt;/p&gt;
guillaume@ubuntu:~$ 
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-AirBnB_clone_v2</code></li>
<li>Directory: <code>web_flask</code></li>
<li>File: <code>6-number_odd_or_even.py, templates/6-number_odd_or_even.html</code></li>
</ul>
</div>

<h3 class="panel-title">
7. Improve engines
</h3>

Before using Flask to display our HBNB data, you will need to update some part of our engine:</p>

<p>Update <code>FileStorage</code>: (<code>models/engine/file_storage.py</code>)</p>

<ul>
<li>Add a public method <code>def close(self):</code>: call <code>reload()</code> method for deserializing the JSON file to objects</li>
</ul>

<p>Update <code>DBStorage</code>: (<code>models/engine/db_storage.py</code>)</p>

<ul>
<li>Add a public method <code>def close(self):</code>: call <code>remove()</code> method on the private session attribute (<code>self.__session</code>) <a href="/rltoken/Ev0jeeBWNlaFqPAFe-rZKA" title="tips" target="_blank">tips</a> or <code>close()</code> on the class <code>Session</code> <a href="/rltoken/d7XXqTOZnNCO47YVh5ZziQ" title="tips" target="_blank">tips</a></li>
</ul>

<p>Update <code>State</code>: (<code>models/state.py</code>) - If it&rsquo;s not already present</p>

<ul>
<li>If your storage engine is not <code>DBStorage</code>, add a public getter method <code>cities</code> to return the list of <code>City</code> objects from <code>storage</code> linked to the current <code>State</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 
&gt;&gt;&gt; from models import storage
&gt;&gt;&gt; from models.state import State
&gt;&gt;&gt; len(storage.all(State))
5
&gt;&gt;&gt; len(storage.all(State))
5
&gt;&gt;&gt; # Time to insert new data!
</code></pre>

<p>At this moment, in another tab:</p>

<pre><code>guillaume@ubuntu:~/AirBnB_v2$ echo &#39;INSERT INTO `states` VALUES (&quot;421a55f1-7d82-45d9-b54c-a76916479545&quot;, &quot;Alabama&quot;, &quot;2017-03-25 19:42:40&quot;,&quot;2017-03-25 19:42:40&quot;);&#39; | mysql -uroot -p hbnb_dev_db
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$ 
</code></pre>

<p>And let&rsquo;s go back the Python console:</p>

<pre><code>&gt;&gt;&gt; # Time to insert new data!
&gt;&gt;&gt; len(storage.all(State))
5
&gt;&gt;&gt; # normal: the SQLAlchemy didn&#39;t reload his `Session`
&gt;&gt;&gt; # to force it, you must remove the current session to create a new one:
&gt;&gt;&gt; storage.close()
&gt;&gt;&gt; len(storage.all(State))
6
&gt;&gt;&gt; # perfect!
</code></pre>

<p>And for the getter <code>cities</code> in the <code>State</code> model:</p>

<pre><code>guillaume@ubuntu:~/AirBnB_v2$ cat main.py
#!/usr/bin/python3
&quot;&quot;&quot;
Test cities access from a state
&quot;&quot;&quot;
from models import storage
from models.state import State
from models.city import City

&quot;&quot;&quot;
Objects creations
&quot;&quot;&quot;
state_1 = State(name=&quot;California&quot;)
print(&quot;New state: {}&quot;.format(state_1))
state_1.save()
state_2 = State(name=&quot;Arizona&quot;)
print(&quot;New state: {}&quot;.format(state_2))
state_2.save()

city_1_1 = City(state_id=state_1.id, name=&quot;Napa&quot;)
print(&quot;New city: {} in the state: {}&quot;.format(city_1_1, state_1))
city_1_1.save()
city_1_2 = City(state_id=state_1.id, name=&quot;Sonoma&quot;)
print(&quot;New city: {} in the state: {}&quot;.format(city_1_2, state_1))
city_1_2.save()
city_2_1 = City(state_id=state_2.id, name=&quot;Page&quot;)
print(&quot;New city: {} in the state: {}&quot;.format(city_2_1, state_2))
city_2_1.save()


&quot;&quot;&quot;
Verification
&quot;&quot;&quot;
print(&quot;&quot;)
all_states = storage.all(State)
for state_id, state in all_states.items():
for city in state.cities:
print(&quot;Find the city {} in the state {}&quot;.format(city, state))

guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ rm file.json ; HBNB_TYPE_STORAGE=fs ./main.py 
New state: [State] (5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45) {&#39;name&#39;: &#39;California&#39;, &#39;id&#39;: &#39;5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45&#39;, &#39;updated_at&#39;: datetime.datetime(2017, 12, 11, 19, 27, 52, 509954), &#39;created_at&#39;: datetime.datetime(2017, 12, 11, 19, 27, 52, 509950)}
New state: [State] (a5e5311a-3c19-4995-9485-32c74411b416) {&#39;name&#39;: &#39;Arizona&#39;, &#39;id&#39;: &#39;a5e5311a-3c19-4995-9485-32c74411b416&#39;, &#39;updated_at&#39;: datetime.datetime(2017, 12, 11, 19, 27, 52, 510256), &#39;created_at&#39;: datetime.datetime(2017, 12, 11, 19, 27, 52, 510252)}
New city: [City] (e3e36ded-fe56-44f5-bf08-8a27e2b30672) {&#39;name&#39;: &#39;Napa&#39;, &#39;id&#39;: &#39;e3e36ded-fe56-44f5-bf08-8a27e2b30672&#39;, &#39;state_id&#39;: &#39;5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45&#39;, &#39;updated_at&#39;: datetime.datetime(2017, 12, 11, 19, 27, 52, 510797), &#39;created_at&#39;: datetime.datetime(2017, 12, 11, 19, 27, 52, 510791)} in the state: [State] (5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45) {&#39;name&#39;: &#39;California&#39;, &#39;id&#39;: &#39;5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45&#39;, &#39;updated_at&#39;: datetime.datetime(2017, 12, 11, 19, 27, 52, 510038), &#39;created_at&#39;: datetime.datetime(2017, 12, 11, 19, 27, 52, 509950)}
New city: [City] (12a58d70-e255-4c1e-8a68-7d5fb924d2d2) {&#39;name&#39;: &#39;Sonoma&#39;, &#39;id&#39;: &#39;12a58d70-e255-4c1e-8a68-7d5fb924d2d2&#39;, &#39;state_id&#39;: &#39;5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45&#39;, &#39;updated_at&#39;: datetime.datetime(2017, 12, 11, 19, 27, 52, 511437), &#39;created_at&#39;: datetime.datetime(2017, 12, 11, 19, 27, 52, 511432)} in the state: [State] (5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45) {&#39;name&#39;: &#39;California&#39;, &#39;id&#39;: &#39;5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45&#39;, &#39;updated_at&#39;: datetime.datetime(2017, 12, 11, 19, 27, 52, 510038), &#39;created_at&#39;: datetime.datetime(2017, 12, 11, 19, 27, 52, 509950)}
New city: [City] (a693bdb9-e0ca-4521-adfd-e1a93c093b4b) {&#39;name&#39;: &#39;Page&#39;, &#39;id&#39;: &#39;a693bdb9-e0ca-4521-adfd-e1a93c093b4b&#39;, &#39;state_id&#39;: &#39;a5e5311a-3c19-4995-9485-32c74411b416&#39;, &#39;updated_at&#39;: datetime.datetime(2017, 12, 11, 19, 27, 52, 511873), &#39;created_at&#39;: datetime.datetime(2017, 12, 11, 19, 27, 52, 511869)} in the state: [State] (a5e5311a-3c19-4995-9485-32c74411b416) {&#39;name&#39;: &#39;Arizona&#39;, &#39;id&#39;: &#39;a5e5311a-3c19-4995-9485-32c74411b416&#39;, &#39;updated_at&#39;: datetime.datetime(2017, 12, 11, 19, 27, 52, 510373), &#39;created_at&#39;: datetime.datetime(2017, 12, 11, 19, 27, 52, 510252)}

Find the city [City] (e3e36ded-fe56-44f5-bf08-8a27e2b30672) {&#39;name&#39;: &#39;Napa&#39;, &#39;id&#39;: &#39;e3e36ded-fe56-44f5-bf08-8a27e2b30672&#39;, &#39;state_id&#39;: &#39;5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45&#39;, &#39;updated_at&#39;: datetime.datetime(2017, 12, 11, 19, 27, 52, 510953), &#39;created_at&#39;: datetime.datetime(2017, 12, 11, 19, 27, 52, 510791)} in the state [State] (5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45) {&#39;name&#39;: &#39;California&#39;, &#39;id&#39;: &#39;5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45&#39;, &#39;updated_at&#39;: datetime.datetime(2017, 12, 11, 19, 27, 52, 510038), &#39;created_at&#39;: datetime.datetime(2017, 12, 11, 19, 27, 52, 509950)}
Find the city [City] (12a58d70-e255-4c1e-8a68-7d5fb924d2d2) {&#39;name&#39;: &#39;Sonoma&#39;, &#39;id&#39;: &#39;12a58d70-e255-4c1e-8a68-7d5fb924d2d2&#39;, &#39;state_id&#39;: &#39;5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45&#39;, &#39;updated_at&#39;: datetime.datetime(2017, 12, 11, 19, 27, 52, 511513), &#39;created_at&#39;: datetime.datetime(2017, 12, 11, 19, 27, 52, 511432)} in the state [State] (5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45) {&#39;name&#39;: &#39;California&#39;, &#39;id&#39;: &#39;5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45&#39;, &#39;updated_at&#39;: datetime.datetime(2017, 12, 11, 19, 27, 52, 510038), &#39;created_at&#39;: datetime.datetime(2017, 12, 11, 19, 27, 52, 509950)}
Find the city [City] (a693bdb9-e0ca-4521-adfd-e1a93c093b4b) {&#39;name&#39;: &#39;Page&#39;, &#39;id&#39;: &#39;a693bdb9-e0ca-4521-adfd-e1a93c093b4b&#39;, &#39;state_id&#39;: &#39;a5e5311a-3c19-4995-9485-32c74411b416&#39;, &#39;updated_at&#39;: datetime.datetime(2017, 12, 11, 19, 27, 52, 512073), &#39;created_at&#39;: datetime.datetime(2017, 12, 11, 19, 27, 52, 511869)} in the state [State] (a5e5311a-3c19-4995-9485-32c74411b416) {&#39;name&#39;: &#39;Arizona&#39;, &#39;id&#39;: &#39;a5e5311a-3c19-4995-9485-32c74411b416&#39;, &#39;updated_at&#39;: datetime.datetime(2017, 12, 11, 19, 27, 52, 510373), &#39;created_at&#39;: datetime.datetime(2017, 12, 11, 19, 27, 52, 510252)}
guillaume@ubuntu:~/AirBnB_v2$ 
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-AirBnB_clone_v2</code></li>
<li>File: <code>models/engine/file_storage.py, models/engine/db_storage.py, models/state.py</code></li>
</ul>
</div>

<h3 class="panel-title">
8. List of states
</h3>

Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>You must use <code>storage</code> for fetching data from the storage engine (<code>FileStorage</code> or <code>DBStorage</code>) =&gt; <code>from models import storage</code> and <code>storage.all(...)</code></li>
<li>After each request you must remove the current SQLAlchemy Session:

<ul>
<li>Declare a method to handle <code>@app.teardown_appcontext</code></li>
<li>Call in this method <code>storage.close()</code></li>
</ul></li>
<li>Routes:

<ul>
<li><code>/states_list</code>: display a HTML page: (inside the tag <code>BODY</code>)

<ul>
<li><code>H1</code> tag: &ldquo;States&rdquo;</li>
<li><code>UL</code> tag: with the list of all <code>State</code> objects present in <code>DBStorage</code> <strong>sorted by <code>name</code></strong> (A-&gt;Z) <a href="/rltoken/UVC1Bw_-nfa_0T2gv1MuQg" title="tip" target="_blank">tip</a>

<ul>
<li><code>LI</code> tag: description of one <code>State</code>: <code>&lt;state.id&gt;: &lt;B&gt;&lt;state.name&gt;&lt;/B&gt;</code></li>
</ul></li>
</ul></li>
</ul></li>
<li><strong>NOTE: Students have reported that this one does not work - use the next on instead.</strong> Import this <a href="https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/290/7-states_list.sql" title="7-dump" target="_blank">7-dump</a> to have some data</li>
<li>Import this <a href="https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/290/100-hbnb.sql" title="100-dump" target="_blank">100-dump</a> to have some data</li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>

<p><strong>IMPORTANT</strong></p>

<ul>
<li>Make sure you have a running and valid <code>setup_mysql_dev.sql</code> in your <code>AirBnB_clone_v2</code> repository (<a href="/rltoken/-Sz0UGvAe4_SLfTbSXSbzg" title="Task" target="_blank">Task</a>)</li>
<li>Make sure all tables are created when you run <code>echo &quot;quit&quot; | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/AirBnB_v2$ curl -o 7-dump.sql &quot;https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/290/100-hbnb.sql&quot;
guillaume@ubuntu:~/AirBnB_v2$ cat 7-dump.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.7-states_list
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In another tab:</p>

<pre><code>guillaume@ubuntu:~$ curl 0.0.0.0:5000/states_list ; echo &quot;&quot;
&lt;!DOCTYPE html&gt;
&lt;HTML lang=&quot;en&quot;&gt;
&lt;HEAD&gt;
&lt;TITLE&gt;HBNB&lt;/TITLE&gt;
&lt;/HEAD&gt;
&lt;BODY&gt;
&lt;H1&gt;States&lt;/H1&gt;
&lt;UL&gt;

&lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479545: &lt;B&gt;Alabama&lt;/B&gt;&lt;/LI&gt;

&lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479546: &lt;B&gt;Arizona&lt;/B&gt;&lt;/LI&gt;

&lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479547: &lt;B&gt;California&lt;/B&gt;&lt;/LI&gt;

&lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479548: &lt;B&gt;Colorado&lt;/B&gt;&lt;/LI&gt;

&lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479549: &lt;B&gt;Florida&lt;/B&gt;&lt;/LI&gt;

&lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479550: &lt;B&gt;Georgia&lt;/B&gt;&lt;/LI&gt;

&lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479551: &lt;B&gt;Hawaii&lt;/B&gt;&lt;/LI&gt;

&lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479552: &lt;B&gt;Illinois&lt;/B&gt;&lt;/LI&gt;

&lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479553: &lt;B&gt;Indiana&lt;/B&gt;&lt;/LI&gt;

&lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479554: &lt;B&gt;Louisiana&lt;/B&gt;&lt;/LI&gt;

&lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479555: &lt;B&gt;Minnesota&lt;/B&gt;&lt;/LI&gt;

&lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479556: &lt;B&gt;Mississippi&lt;/B&gt;&lt;/LI&gt;

&lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479557: &lt;B&gt;Oregon&lt;/B&gt;&lt;/LI&gt;

&lt;/UL&gt;
&lt;/BODY&gt;
&lt;/HTML&gt;
guillaume@ubuntu:~$ 
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-AirBnB_clone_v2</code></li>
<li>File: <code>web_flask/7-states_list.py, web_flask/templates/7-states_list.html</code></li>
</ul>
</div>

<h3 class="panel-title">
9. Cities by states
</h3>

Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>You must use <code>storage</code> for fetching data from the storage engine (<code>FileStorage</code> or <code>DBStorage</code>) =&gt; <code>from models import storage</code> and <code>storage.all(...)</code></li>
<li>To load all cities of a <code>State</code>:

<ul>
<li>If your storage engine is <code>DBStorage</code>, you must use <code>cities</code> relationship</li>
<li>Otherwise, use the public getter method <code>cities</code></li>
</ul></li>
<li>After each request you must remove the current SQLAlchemy Session:

<ul>
<li>Declare a method to handle <code>@app.teardown_appcontext</code></li>
<li>Call in this method <code>storage.close()</code></li>
</ul></li>
<li>Routes:

<ul>
<li><code>/cities_by_states</code>: display a HTML page: (inside the tag <code>BODY</code>)

<ul>
<li><code>H1</code> tag: &ldquo;States&rdquo;</li>
<li><code>UL</code> tag: with the list of all <code>State</code> objects present in <code>DBStorage</code> <strong>sorted by <code>name</code></strong> (A-&gt;Z) <a href="/rltoken/UVC1Bw_-nfa_0T2gv1MuQg" title="tip" target="_blank">tip</a>

<ul>
<li><code>LI</code> tag: description of one <code>State</code>: <code>&lt;state.id&gt;: &lt;B&gt;&lt;state.name&gt;&lt;/B&gt;</code> + <code>UL</code> tag: with the list of <code>City</code> objects linked to the <code>State</code> <strong>sorted by <code>name</code></strong> (A-&gt;Z)

<ul>
<li><code>LI</code> tag: description of one <code>City</code>: <code>&lt;city.id&gt;: &lt;B&gt;&lt;city.name&gt;&lt;/B&gt;</code></li>
</ul></li>
</ul></li>
</ul></li>
</ul></li>
<li><strong>NOTE: Students have reported that this one does not work - use the next on instead.</strong> Import this <a href="https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/290/7-states_list.sql" title="7-dump" target="_blank">7-dump</a> to have some data</li>
<li>Import this <a href="https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/290/100-hbnb.sql" title="100-dump" target="_blank">100-dump</a> to have some data</li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>

<p><strong>IMPORTANT</strong></p>

<ul>
<li>Make sure you have a running and valid <code>setup_mysql_dev.sql</code> in your <code>AirBnB_clone_v2</code> repository (<a href="/rltoken/gIfF4l2eWBO13bfNduSG4w" title="Task" target="_blank">Task</a>)</li>
<li>Make sure all tables are created when you run <code>echo &quot;quit&quot; | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/AirBnB_v2$ curl -o 7-dump.sql &quot;https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/290/100-hbnb.sql&quot;
guillaume@ubuntu:~/AirBnB_v2$ cat 7-dump.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.8-cities_by_states
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In another tab:</p>

<pre><code>guillaume@ubuntu:~$ curl 0.0.0.0:5000/cities_by_states ; echo &quot;&quot;
&lt;!DOCTYPE html&gt;
&lt;HTML lang=&quot;en&quot;&gt;
&lt;HEAD&gt;
&lt;TITLE&gt;HBNB&lt;/TITLE&gt;
&lt;/HEAD&gt;
&lt;BODY&gt;
&lt;H1&gt;States&lt;/H1&gt;
&lt;UL&gt;

&lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479545: &lt;B&gt;Alabama&lt;/B&gt;
&lt;UL&gt;

&lt;LI&gt;521a55f4-7d82-47d9-b54c-a76916479545: &lt;B&gt;Akron&lt;/B&gt;&lt;/LI&gt;

&lt;LI&gt;531a55f4-7d82-47d9-b54c-a76916479545: &lt;B&gt;Babbie&lt;/B&gt;&lt;/LI&gt;

&lt;LI&gt;541a55f4-7d82-47d9-b54c-a76916479545: &lt;B&gt;Calera&lt;/B&gt;&lt;/LI&gt;

&lt;LI&gt;551a55f4-7d82-47d9-b54c-a76916479545: &lt;B&gt;Fairfield&lt;/B&gt;&lt;/LI&gt;

&lt;/UL&gt;
&lt;/LI&gt;

&lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479546: &lt;B&gt;Arizona&lt;/B&gt;
&lt;UL&gt;

&lt;LI&gt;521a55f4-7d82-47d9-b54c-a76916479546: &lt;B&gt;Douglas&lt;/B&gt;&lt;/LI&gt;

&lt;LI&gt;531a55f4-7d82-47d9-b54c-a76916479546: &lt;B&gt;Kearny&lt;/B&gt;&lt;/LI&gt;

&lt;LI&gt;541a55f4-7d82-47d9-b54c-a76916479546: &lt;B&gt;Tempe&lt;/B&gt;&lt;/LI&gt;

&lt;/UL&gt;
&lt;/LI&gt;

&lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479547: &lt;B&gt;California&lt;/B&gt;
&lt;UL&gt;

&lt;LI&gt;541a55f4-7d82-47d9-b54c-a76916479547: &lt;B&gt;Fremont&lt;/B&gt;&lt;/LI&gt;

&lt;LI&gt;551a55f4-7d82-47d9-b54c-a76916479547: &lt;B&gt;Napa&lt;/B&gt;&lt;/LI&gt;

&lt;LI&gt;521a55f4-7d82-47d9-b54c-a76916479547: &lt;B&gt;San Francisco&lt;/B&gt;&lt;/LI&gt;

&lt;LI&gt;531a55f4-7d82-47d9-b54c-a76916479547: &lt;B&gt;San Jose&lt;/B&gt;&lt;/LI&gt;

&lt;LI&gt;561a55f4-7d82-47d9-b54c-a76916479547: &lt;B&gt;Sonoma&lt;/B&gt;&lt;/LI&gt;

&lt;/UL&gt;
&lt;/LI&gt;

&lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479548: &lt;B&gt;Colorado&lt;/B&gt;
&lt;UL&gt;

&lt;LI&gt;521a55f4-7d82-47d9-b54c-a76916479548: &lt;B&gt;Denver&lt;/B&gt;&lt;/LI&gt;

&lt;/UL&gt;
&lt;/LI&gt;

&lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479549: &lt;B&gt;Florida&lt;/B&gt;
&lt;UL&gt;

&lt;LI&gt;521a55f4-7d82-47d9-b54c-a76916479549: &lt;B&gt;Miami&lt;/B&gt;&lt;/LI&gt;

&lt;LI&gt;531a55f4-7d82-47d9-b54c-a76916479549: &lt;B&gt;Orlando&lt;/B&gt;&lt;/LI&gt;

&lt;/UL&gt;
&lt;/LI&gt;

&lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479550: &lt;B&gt;Georgia&lt;/B&gt;
&lt;UL&gt;

&lt;/UL&gt;
&lt;/LI&gt;

&lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479551: &lt;B&gt;Hawaii&lt;/B&gt;
&lt;UL&gt;

&lt;LI&gt;521a55f4-7d82-47d9-b54c-a76916479551: &lt;B&gt;Honolulu&lt;/B&gt;&lt;/LI&gt;

&lt;LI&gt;531a55f4-7d82-47d9-b54c-a76916479551: &lt;B&gt;Kailua&lt;/B&gt;&lt;/LI&gt;

&lt;LI&gt;541a55f4-7d82-47d9-b54c-a76916479551: &lt;B&gt;Pearl city&lt;/B&gt;&lt;/LI&gt;

&lt;/UL&gt;
&lt;/LI&gt;

&lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479552: &lt;B&gt;Illinois&lt;/B&gt;
&lt;UL&gt;

&lt;LI&gt;521a55f4-7d82-47d9-b54c-a76916479552: &lt;B&gt;Chicago&lt;/B&gt;&lt;/LI&gt;

&lt;LI&gt;561a55f4-7d82-47d9-b54c-a76916479552: &lt;B&gt;Joliet&lt;/B&gt;&lt;/LI&gt;

&lt;LI&gt;541a55f4-7d82-47d9-b54c-a76916479552: &lt;B&gt;Naperville&lt;/B&gt;&lt;/LI&gt;

&lt;LI&gt;531a55f4-7d82-47d9-b54c-a76916479552: &lt;B&gt;Peoria&lt;/B&gt;&lt;/LI&gt;

&lt;LI&gt;551a55f4-7d82-47d9-b54c-a76916479552: &lt;B&gt;Urbana&lt;/B&gt;&lt;/LI&gt;

&lt;/UL&gt;
&lt;/LI&gt;

&lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479553: &lt;B&gt;Indiana&lt;/B&gt;
&lt;UL&gt;

&lt;/UL&gt;
&lt;/LI&gt;

&lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479554: &lt;B&gt;Louisiana&lt;/B&gt;
&lt;UL&gt;

&lt;LI&gt;531a55f4-7d82-47d9-b54c-a76916479554: &lt;B&gt;Baton rouge&lt;/B&gt;&lt;/LI&gt;

&lt;LI&gt;541a55f4-7d82-47d9-b54c-a76916479554: &lt;B&gt;Lafayette&lt;/B&gt;&lt;/LI&gt;

&lt;LI&gt;521a55f4-7d82-47d9-b54c-a76916479554: &lt;B&gt;New Orleans&lt;/B&gt;&lt;/LI&gt;

&lt;/UL&gt;
&lt;/LI&gt;

&lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479555: &lt;B&gt;Minnesota&lt;/B&gt;
&lt;UL&gt;

&lt;LI&gt;521a55f4-7d82-47d9-b54c-a76916479555: &lt;B&gt;Saint Paul&lt;/B&gt;&lt;/LI&gt;

&lt;/UL&gt;
&lt;/LI&gt;

&lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479556: &lt;B&gt;Mississippi&lt;/B&gt;
&lt;UL&gt;

&lt;LI&gt;521a55f4-7d82-47d9-b54c-a76916479556: &lt;B&gt;Jackson&lt;/B&gt;&lt;/LI&gt;

&lt;LI&gt;541a55f4-7d82-47d9-b54c-a76916479556: &lt;B&gt;Meridian&lt;/B&gt;&lt;/LI&gt;

&lt;LI&gt;531a55f4-7d82-47d9-b54c-a76916479556: &lt;B&gt;Tupelo&lt;/B&gt;&lt;/LI&gt;

&lt;/UL&gt;
&lt;/LI&gt;

&lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479557: &lt;B&gt;Oregon&lt;/B&gt;
&lt;UL&gt;

&lt;LI&gt;531a55f4-7d82-47d9-b54c-a76916479557: &lt;B&gt;Eugene&lt;/B&gt;&lt;/LI&gt;

&lt;LI&gt;521a55f4-7d82-47d9-b54c-a76916479557: &lt;B&gt;Portland&lt;/B&gt;&lt;/LI&gt;

&lt;/UL&gt;
&lt;/LI&gt;

&lt;/UL&gt;
&lt;/BODY&gt;
&lt;/HTML&gt;
guillaume@ubuntu:~$ 
</code></pre>

<p><img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/9/9a7ae8155274b17881442200437e8793cf08de48.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20231211%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20231211T130624Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=c13ef9964e37e70c463d814c1e4014c0e99eaec4dc77bc040e1ebb614fe1bb81" alt="" loading='lazy' style="" /></p>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-AirBnB_clone_v2</code></li>
<li>File: <code>web_flask/8-cities_by_states.py, web_flask/templates/8-cities_by_states.html</code></li>
</ul>
</div>

<h3 class="panel-title">
10. States and State
</h3>

Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>You must use <code>storage</code> for fetching data from the storage engine (<code>FileStorage</code> or <code>DBStorage</code>) =&gt; <code>from models import storage</code> and <code>storage.all(...)</code></li>
<li>To load all cities of a <code>State</code>:

<ul>
<li>If your storage engine is <code>DBStorage</code>, you must use <code>cities</code> relationship</li>
<li>Otherwise, use the public getter method <code>cities</code></li>
</ul></li>
<li>After each request you must remove the current SQLAlchemy Session:

<ul>
<li>Declare a method to handle <code>@app.teardown_appcontext</code></li>
<li>Call in this method <code>storage.close()</code></li>
</ul></li>
<li>Routes:

<ul>
<li><code>/states</code>: display a HTML page: (inside the tag <code>BODY</code>)

<ul>
<li><code>H1</code> tag: &ldquo;States&rdquo;</li>
<li><code>UL</code> tag: with the list of all <code>State</code> objects present in <code>DBStorage</code> <strong>sorted by <code>name</code></strong> (A-&gt;Z) <a href="/rltoken/UVC1Bw_-nfa_0T2gv1MuQg" title="tip" target="_blank">tip</a>

<ul>
<li><code>LI</code> tag: description of one <code>State</code>: <code>&lt;state.id&gt;: &lt;B&gt;&lt;state.name&gt;&lt;/B&gt;</code></li>
</ul></li>
</ul></li>
<li><code>/states/&lt;id&gt;</code>: display a HTML page: (inside the tag <code>BODY</code>)

<ul>
<li>If a <code>State</code> object is found with this <code>id</code>:

<ul>
<li><code>H1</code> tag: &ldquo;State: <state.name>&rdquo;</li>
<li><code>H3</code> tag: &ldquo;Cities:&rdquo;</li>
<li><code>UL</code> tag: with the list of <code>City</code> objects linked to the <code>State</code> <strong>sorted by <code>name</code></strong> (A-&gt;Z)

<ul>
<li><code>LI</code> tag: description of one <code>City</code>: <code>&lt;city.id&gt;: &lt;B&gt;&lt;city.name&gt;&lt;/B&gt;</code></li>
</ul></li>
</ul></li>
<li>Otherwise: 

<ul>
<li><code>H1</code> tag: &ldquo;Not found!&rdquo;</li>
</ul></li>
</ul></li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
<li><strong>NOTE: Students have reported that this one does not work - use the next on instead.</strong> Import this <a href="https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/290/7-states_list.sql" title="7-dump" target="_blank">7-dump</a> to have some data</li>
<li>Import this <a href="https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/290/100-hbnb.sql" title="100-dump" target="_blank">100-dump</a> to have some data</li>
</ul>

<p><strong>IMPORTANT</strong></p>

<ul>
<li>Make sure you have a running and valid <code>setup_mysql_dev.sql</code> in your <code>AirBnB_clone_v2</code> repository (<a href="/rltoken/gIfF4l2eWBO13bfNduSG4w" title="Task" target="_blank">Task</a>)</li>
<li>Make sure all tables are created when you run <code>echo &quot;quit&quot; | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/AirBnB_v2$ curl -o 7-dump.sql &quot;https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/290/100-hbnb.sql&quot;
guillaume@ubuntu:~/AirBnB_v2$ cat 7-dump.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.9-states
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In another tab:</p>

<pre><code>guillaume@ubuntu:~$ curl 0.0.0.0:5000/states ; echo &quot;&quot;
&lt;!DOCTYPE html&gt;
&lt;HTML lang=&quot;en&quot;&gt;
&lt;HEAD&gt;
&lt;TITLE&gt;HBNB&lt;/TITLE&gt;
&lt;/HEAD&gt;
&lt;BODY&gt;

&lt;H1&gt;States&lt;/H1&gt;
&lt;UL&gt;

&lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479545: &lt;B&gt;Alabama&lt;/B&gt;&lt;/LI&gt;

&lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479546: &lt;B&gt;Arizona&lt;/B&gt;&lt;/LI&gt;

&lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479547: &lt;B&gt;California&lt;/B&gt;&lt;/LI&gt;

&lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479548: &lt;B&gt;Colorado&lt;/B&gt;&lt;/LI&gt;

&lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479549: &lt;B&gt;Florida&lt;/B&gt;&lt;/LI&gt;

&lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479550: &lt;B&gt;Georgia&lt;/B&gt;&lt;/LI&gt;

&lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479551: &lt;B&gt;Hawaii&lt;/B&gt;&lt;/LI&gt;

&lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479552: &lt;B&gt;Illinois&lt;/B&gt;&lt;/LI&gt;

&lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479553: &lt;B&gt;Indiana&lt;/B&gt;&lt;/LI&gt;

&lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479554: &lt;B&gt;Louisiana&lt;/B&gt;&lt;/LI&gt;

&lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479555: &lt;B&gt;Minnesota&lt;/B&gt;&lt;/LI&gt;

&lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479556: &lt;B&gt;Mississippi&lt;/B&gt;&lt;/LI&gt;

&lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479557: &lt;B&gt;Oregon&lt;/B&gt;&lt;/LI&gt;

&lt;/UL&gt;

&lt;/BODY&gt;
&lt;/HTML&gt;
guillaume@ubuntu:~$ curl 0.0.0.0:5000/states/421a55f4-7d82-47d9-b54c-a76916479552 ; echo &quot;&quot;
&lt;!DOCTYPE html&gt;
&lt;HTML lang=&quot;en&quot;&gt;
&lt;HEAD&gt;
&lt;TITLE&gt;HBNB&lt;/TITLE&gt;
&lt;/HEAD&gt;
&lt;BODY&gt;

&lt;H1&gt;State: Illinois&lt;/H1&gt;
&lt;H3&gt;Cities:&lt;/H3&gt;
&lt;UL&gt;
&lt;LI&gt;521a55f4-7d82-47d9-b54c-a76916479552: &lt;B&gt;Chicago&lt;/B&gt;&lt;/LI&gt;

&lt;LI&gt;561a55f4-7d82-47d9-b54c-a76916479552: &lt;B&gt;Joliet&lt;/B&gt;&lt;/LI&gt;

&lt;LI&gt;541a55f4-7d82-47d9-b54c-a76916479552: &lt;B&gt;Naperville&lt;/B&gt;&lt;/LI&gt;

&lt;LI&gt;531a55f4-7d82-47d9-b54c-a76916479552: &lt;B&gt;Peoria&lt;/B&gt;&lt;/LI&gt;

&lt;LI&gt;551a55f4-7d82-47d9-b54c-a76916479552: &lt;B&gt;Urbana&lt;/B&gt;&lt;/LI&gt;
&lt;/UL&gt;

&lt;/BODY&gt;
&lt;/HTML&gt;
guillaume@ubuntu:~$ curl 0.0.0.0:5000/states/holberton ; echo &quot;&quot;
&lt;!DOCTYPE html&gt;
&lt;HTML lang=&quot;en&quot;&gt;
&lt;HEAD&gt;
&lt;TITLE&gt;HBNB&lt;/TITLE&gt;
&lt;/HEAD&gt;
&lt;BODY&gt;

&lt;H1&gt;Not found!&lt;/H1&gt;

&lt;/BODY&gt;
&lt;/HTML&gt;
guillaume@ubuntu:~$ 
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-AirBnB_clone_v2</code></li>
<li>File: <code>web_flask/9-states.py, web_flask/templates/9-states.html</code></li>
</ul>
</div>

<h3 class="panel-title">
11. HBNB filters
</h3>

Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>You must use <code>storage</code> for fetching data from the storage engine (<code>FileStorage</code> or <code>DBStorage</code>) =&gt; <code>from models import storage</code> and <code>storage.all(...)</code></li>
<li>To load all cities of a <code>State</code>:

<ul>
<li>If your storage engine is <code>DBStorage</code>, you must use <code>cities</code> relationship</li>
<li>Otherwise, use the public getter method <code>cities</code></li>
</ul></li>
<li>After each request you must remove the current SQLAlchemy Session:

<ul>
<li>Declare a method to handle <code>@app.teardown_appcontext</code></li>
<li>Call in this method <code>storage.close()</code></li>
</ul></li>
<li>Routes:

<ul>
<li><code>/hbnb_filters</code>: display a HTML page like <code>6-index.html</code>, which was done during the project <a href="/rltoken/LSsy0WYsMdxl-zlZqbAthg" title="0x01. AirBnB clone - Web static" target="_blank">0x01. AirBnB clone - Web static</a>

<ul>
<li>Copy files <code>3-footer.css</code>, <code>3-header.css</code>, <code>4-common.css</code> and <code>6-filters.css</code> from <code>web_static/styles/</code> to the folder <code>web_flask/static/styles</code></li>
<li>Copy files <code>icon.png</code> and <code>logo.png</code> from <code>web_static/images/</code> to the folder <code>web_flask/static/images</code></li>
<li>Update <code>.popover</code> class in <code>6-filters.css</code> to allow scrolling in the popover and a max height of 300 pixels.</li>
<li>Use <code>6-index.html</code> content as source code for the template <code>10-hbnb_filters.html</code>:

<ul>
<li>Replace the content of the <code>H4</code> tag under each filter title (<code>H3</code> States and <code>H3</code> Amenities) by <code>&amp;nbsp;</code></li>
</ul></li>
<li><code>State</code>, <code>City</code> and <code>Amenity</code> objects must be loaded from <code>DBStorage</code> and <strong>sorted by name</strong> (A-&gt;Z)</li>
</ul></li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
<li>Import this <a href="https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/290/10-hbnb_filters.sql" title="10-dump" target="_blank">10-dump</a> to have some data</li>
</ul>

<p><strong>IMPORTANT</strong></p>

<ul>
<li>Make sure you have a running and valid <code>setup_mysql_dev.sql</code> in your <code>AirBnB_clone_v2</code> repository (<a href="/rltoken/gIfF4l2eWBO13bfNduSG4w" title="Task" target="_blank">Task</a>)</li>
<li>Make sure all tables are created when you run <code>echo &quot;quit&quot; | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/AirBnB_v2$ curl -o 10-dump.sql &quot;https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/290/10-hbnb_filters.sql&quot;
guillaume@ubuntu:~/AirBnB_v2$ cat 10-dump.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.10-hbnb_filters
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In the browser:</p>

<p><img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/9/4f993ec8ca2a2f639a80887667106ac63a0a3701.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20231211%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20231211T130624Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=5fcc6e80ebaf0aefbc79c1670f7c395ebfcc6b9df604cd8e585b912394ad15a6" alt="" loading='lazy' style="" />
<img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/9/1549b553d726cc37f64440be910cb6b858aa32ae.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20231211%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20231211T130624Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=4a503b735ed80e1dcc2479de67043fe9444b0f0e80da6eb937a1336bd13673b1" alt="" loading='lazy' style="" />
<img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/9/94b3a416ba1551c59701eb6672ac0a36fbebba14.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20231211%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20231211T130624Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=1652e57dbc4846a0a6964f8824883cbd5a6920593837dd8498847a6f13d63aab" alt="" loading='lazy' style="" />
<img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/9/1e559707dd34a37564dc10e54b707815a516d363.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20231211%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20231211T130624Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=93b775f22beb681a5ad170a7a8ba12175d2097735a4ec7c439a59d87a946e08c" alt="" loading='lazy' style="" /></p>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-AirBnB_clone_v2</code></li>
<li>File: <code>web_flask/10-hbnb_filters.py, web_flask/templates/10-hbnb_filters.html, web_flask/static/</code></li>
</ul>
</div>

</details>
