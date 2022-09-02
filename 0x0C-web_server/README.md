<div class="col-xs-12 col-md-10 col-lg-8 contains-images">

      <h1 class="gap">0x0C. Web server</h1>

  <div data-react-class="tags/Tags" data-react-props="{&quot;tags&quot;:[]}" data-react-cache-id="tags/Tags-0"></div>

  <div data-react-class="projects/ProjectMetadata" data-react-props="{&quot;metadata&quot;:{&quot;author&quot;:&quot;Sylvain Kalache&quot;,&quot;weight&quot;:1,&quot;correction&quot;:{&quot;released&quot;:true,&quot;requires_auto_correction&quot;:true,&quot;requires_manual_correction&quot;:true,&quot;manual_done_at&quot;:&quot;2022-09-01T03:15:15.000-05:00&quot;},&quot;bpi&quot;:{&quot;current&quot;:false,&quot;in_second_deadline&quot;:false,&quot;starts_at&quot;:&quot;2022-08-22T00:00:00.000-05:00&quot;,&quot;ends_at&quot;:&quot;2022-08-24T00:00:00.000-05:00&quot;,&quot;second_deadline_at&quot;:&quot;2022-08-25T00:00:00.000-05:00&quot;}}}" data-react-cache-id="projects/ProjectMetadata-0"><ul class="list-group metadata" id="project-metadata"><li class="list-group-item"><i aria-hidden="true" class="fa fa-user fa-fw"></i> By: Sylvain Kalache</li><li class="list-group-item"><i aria-hidden="true" class="fa fa-cog fa-fw"></i> Weight: 1</li><li class="list-group-item"><i aria-hidden="true" class="fa fa-calendar fa-fw"></i> Project over - took place from <span data-container="body" data-html="false" data-placement="auto top" data-toggle="tooltip" title="" data-original-title="2022-08-22 00:00 (GMT-05:00)"><span class="datetime">Aug 22, 2022 12:00 AM</span></span> to <span data-container="body" data-html="false" data-placement="auto top" data-toggle="tooltip" title="" data-original-title="2022-08-24 00:00 (GMT-05:00)"><span class="datetime">Aug 24, 2022 12:00 AM</span></span></li><li class="list-group-item"><i aria-hidden="true" class="fa fa-check-square fa-fw"></i> Manual QA review was done by  on <span data-container="body" data-html="false" data-placement="auto top" data-toggle="tooltip" title="" data-original-title="2022-09-01 03:15 (GMT-05:00)"><span class="datetime">Sep 1, 2022 3:15 AM</span></span></li><li class="list-group-item"><i aria-hidden="true" class="fa fa-check-square fa-fw"></i> An auto review will be launched at the deadline</li></ul></div>

  <div class="sm-gap clean well">
  <h4>In a nutshell…</h4>
  <ul>

      <li>
        <strong>Manual QA review:</strong>
          0.0/0 mandatory
            &amp;
            0.0/2 optional
      </li>

      <li>
        <strong>Auto QA review:</strong>
          10.0/13 mandatory
            &amp;
            0.0/4 optional
      </li>
    <li>
      <strong>Altogether:</strong>
        &nbsp;<strong>76.92%</strong>
        <ul>
          <li>Mandatory: 76.92%</li>
            <li>Optional: 0.0%</li>
            <li>
              Calculation:&nbsp;
                  76.92%
                    + (76.92% * 0.0%)
              &nbsp;==&nbsp;<strong>76.92%</strong>
            </li>
        </ul>
    </li>
  </ul>
</div>





    <div id="project_id" style="display: none" data-project-id="266"></div>



      

      

      <div class="panel panel-default" id="project-description">
  <div class="panel-body">
    <p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/8Gu52Qv.png" alt="" loading="lazy" style=""></p>

<h2>Background Context</h2>

<p><a href="https://www.youtube.com/watch?v=AZg4uJkEa-4&amp;feature=youtu.be&amp;hd=1" target="_blank"><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/Screenshot+2017-07-06+19.24.05.png" alt="" loading="lazy" style=""></a></p>

<p>In this project, some of the tasks will be graded on 2 aspects:</p>

<ol>
<li>Is your <code>web-01</code> server configured according to requirements</li>
<li>Does your answer file contain a Bash script that automatically performs commands to configure an Ubuntu machine to fit requirements (meaning without any human intervention)</li>
</ol>

<p>For example, if I need to create a file <code>/tmp/test</code> containing the string <code>hello world</code> and modify the configuration of Nginx to listen on port <code>8080</code> instead of <code>80</code>, I can use <code>emacs</code> on my server to create the file and to modify the Nginx configuration file <code>/etc/nginx/sites-enabled/default</code>.</p>

<p>But my answer file would contain:</p>

<pre><code>sylvain@ubuntu cat 88-script_example
#!/usr/bin/env bash
# Configuring a server with specification XYZ
echo hello world &gt; /tmp/test
sed -i 's/80/8080/g' /etc/nginx/sites-enabled/default
sylvain@ubuntu
</code></pre>

<p>As you can tell, I am not using <code>emacs</code> to perform the task in my answer file. This exercise is aiming at training you on automating your work. If you can automate tasks that you do manually, you can then automate yourself out of repetitive tasks and focus your energy on something more interesting. For an <a href="/rltoken/Hjv9yJQtW6X7VRa2ByMeEg" title="SRE" target="_blank">SRE</a>, that comes very handy when there are hundreds or thousands of servers to manage, the work cannot be only done manually. Note that the checker will execute your script as the <code>root</code> user, you do not need to use the <code>sudo</code> command.</p>

<p>A good Software Engineer is a <a href="/rltoken/y1MX-uAX-0a4bgXfH3uweQ" title="lazy Software Engineer" target="_blank">lazy Software Engineer</a>.
<img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/82VsYEC.jpg" alt="" loading="lazy" style=""></p>

<p>Tips: to test your answer Bash script, feel free to reproduce the checker environment: </p>

<ul>
<li>start a <code>Ubuntu 16.04</code> sandbox</li>
<li>run your script on it</li>
<li>see how it behaves</li>
</ul>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/4tRRzyyETAySzU-bgNGLSw" title="How the web works" target="_blank">How the web works</a> </li>
<li><a href="/rltoken/H9OfhUnBDdxV-QQnIucMlA" title="Nginx" target="_blank">Nginx</a> </li>
<li><a href="/rltoken/wePwmjbJDgJZO7YPvffWxQ" title="How to Configure Nginx" target="_blank">How to Configure Nginx</a></li>
<li><strong>Child process</strong> concept page</li>
<li><a href="/rltoken/S2JO8E1CftLXOgvCfYf78A" title="Root and sub domain" target="_blank">Root and sub domain</a> </li>
<li><a href="/rltoken/C9s3U62JbiOAvn9WCoxKsA" title="HTTP requests" target="_blank">HTTP requests</a> </li>
<li><a href="/rltoken/kI4vRQ6vc45Wfbdo3UD8Lw" title="HTTP redirection" target="_blank">HTTP redirection</a> </li>
<li><a href="/rltoken/5UvC588x2hZR7dm6eRFPoQ" title="Not found HTTP response code" target="_blank">Not found HTTP response code</a> </li>
<li><a href="/rltoken/bkqQ72HZVAV65G8nB503Pw" title="Logs files on Linux" target="_blank">Logs files on Linux</a> </li>
</ul>

<p><strong>For reference:</strong></p>

<ul>
<li><a href="/rltoken/Ip0atFgh-X8dcQxQdUyVUA" title="RFC 7231 (HTTP/1.1)" target="_blank">RFC 7231 (HTTP/1.1)</a></li>
<li><a href="/rltoken/cwfqkSHy98XGvyezL5KIIA" title="RFC 7540 (HTTP/2)" target="_blank">RFC 7540 (HTTP/2)</a></li>
</ul>

<p><strong>man or help</strong>: </p>

<ul>
<li><code>scp</code></li>
<li><code>curl</code></li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/HLB_f8cKD3VOdBgXcaHTdA" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What is the main role of a web server</li>
<li>What is a child process</li>
<li>Why web servers usually have a parent process and child processes</li>
<li>What are the main HTTP requests</li>
</ul>

<h3>DNS</h3>

<ul>
<li>What DNS stands for</li>
<li>What is DNS main role</li>
</ul>

<h3>DNS Record Types</h3>

<ul>
<li><code>A</code></li>
<li><code>CNAME</code></li>
<li><code>TXT</code></li>
<li><code>MX</code></li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted on Ubuntu 16.04 LTS</li>
<li>All your files should end with a new line</li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>All your Bash script files must be executable</li>
<li>Your Bash script must pass <code>Shellcheck</code> (version <code>0.3.7</code>) without any error</li>
<li>The first line of all your Bash scripts should be exactly <code>#!/usr/bin/env bash</code></li>
<li>The second line of all your Bash scripts should be a comment explaining what is the script doing</li>
<li>You can’t use <code>systemctl</code> for restarting a process</li>
</ul>

  </div>
</div>


      

        <div class="panel panel-default" id="project-quiz-questions-title">
    <div class="panel-heading">
      <h3 class="panel-title">
        Quiz questions
      </h3>
    </div>

    <div class="panel-body">

        <div class="alert alert-info">
          <strong>Great!</strong>
          You've completed the quiz successfully! Keep going!
          <span id="quiz_questions_collapse_toggle">(Show quiz)</span>
        </div>

      <section class="quiz_questions_show_container" style="display: none;">
          <div class="quiz_question_item_container" data-role="quiz_question516" data-position="1">
            <div class=" clearfix" id="quiz_question-516">

    <h4 class="quiz_question">
        
        Question #0
    </h4>

    <!-- Quiz question Body -->
    <p>The main role of a web server is to</p>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="516">
                <li class="">

  <input type="radio" name="516" id="516-1509572684973" value="1509572684973" data-quiz-answer-id="1509572684973" data-quiz-question-id="516" disabled="disabled">
  <label for="516-1509572684973"><p>serve dynamic content</p>
</label>
</li>

                <li class="">

  <input type="radio" name="516" id="516-1509572704804" value="1509572704804" data-quiz-answer-id="1509572704804" data-quiz-question-id="516" disabled="disabled" checked="checked">
  <label for="516-1509572704804"><p>serve static content</p>
</label>
</li>

                <li class="">

  <input type="radio" name="516" id="516-1509572712795" value="1509572712795" data-quiz-answer-id="1509572712795" data-quiz-question-id="516" disabled="disabled">
  <label for="516-1509572712795"><p>host files</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question518" data-position="2">
            <div class=" clearfix" id="quiz_question-518">

    <h4 class="quiz_question">
        
        Question #1
    </h4>

    <!-- Quiz question Body -->
    <p>A web server is</p>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="518">
                <li class="">

  <input type="radio" name="518" id="518-1509573022485" value="1509573022485" data-quiz-answer-id="1509573022485" data-quiz-question-id="518" disabled="disabled">
  <label for="518-1509573022485"><p>a physical machine</p>
</label>
</li>

                <li class="">

  <input type="radio" name="518" id="518-1509573028589" value="1509573028589" data-quiz-answer-id="1509573028589" data-quiz-question-id="518" disabled="disabled" checked="checked">
  <label for="518-1509573028589"><p>a software</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question519" data-position="3">
            <div class=" clearfix" id="quiz_question-519">

    <h4 class="quiz_question">
        
        Question #2
    </h4>

    <!-- Quiz question Body -->
    <p>The main role of DNS is to</p>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="519">
                <li class="">

  <input type="radio" name="519" id="519-1509575404721" value="1509575404721" data-quiz-answer-id="1509575404721" data-quiz-question-id="519" disabled="disabled" checked="checked">
  <label for="519-1509575404721"><p>translate domain name into IP address</p>
</label>
</li>

                <li class="">

  <input type="radio" name="519" id="519-1509575417553" value="1509575417553" data-quiz-answer-id="1509575417553" data-quiz-question-id="519" disabled="disabled">
  <label for="519-1509575417553"><p>translate domain name into port</p>
</label>
</li>

                <li class="">

  <input type="radio" name="519" id="519-1509575435322" value="1509575435322" data-quiz-answer-id="1509575435322" data-quiz-question-id="519" disabled="disabled">
  <label for="519-1509575435322"><p>name websites</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question520" data-position="4">
            <div class=" clearfix" id="quiz_question-520">

    <h4 class="quiz_question">
        
        Question #3
    </h4>

    <!-- Quiz question Body -->
    <p>What was one of the most important reason for which DNS was created</p>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="520">
                <li class="">

  <input type="radio" name="520" id="520-1509575510693" value="1509575510693" data-quiz-answer-id="1509575510693" data-quiz-question-id="520" disabled="disabled" checked="checked">
  <label for="520-1509575510693"><p>because humans are not good at remembering long sequences of numbers (IP address)</p>
</label>
</li>

                <li class="">

  <input type="radio" name="520" id="520-1509575529400" value="1509575529400" data-quiz-answer-id="1509575529400" data-quiz-question-id="520" disabled="disabled">
  <label for="520-1509575529400"><p>to connect the Internet</p>
</label>
</li>

                <li class="">

  <input type="radio" name="520" id="520-1509575552513" value="1509575552513" data-quiz-answer-id="1509575552513" data-quiz-question-id="520" disabled="disabled">
  <label for="520-1509575552513"><p>to index the web</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question521" data-position="5">
            <div class=" clearfix" id="quiz_question-521">

    <h4 class="quiz_question">
        
        Question #4
    </h4>

    <!-- Quiz question Body -->
    <p>A HTTP GET request is to</p>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="521">
                <li class="">

  <input type="radio" name="521" id="521-1509575983467" value="1509575983467" data-quiz-answer-id="1509575983467" data-quiz-question-id="521" disabled="disabled" checked="checked">
  <label for="521-1509575983467"><p>request data</p>
</label>
</li>

                <li class="">

  <input type="radio" name="521" id="521-1509575994654" value="1509575994654" data-quiz-answer-id="1509575994654" data-quiz-question-id="521" disabled="disabled">
  <label for="521-1509575994654"><p>submit data</p>
</label>
</li>

                <li class="">

  <input type="radio" name="521" id="521-1509576005855" value="1509576005855" data-quiz-answer-id="1509576005855" data-quiz-question-id="521" disabled="disabled">
  <label for="521-1509576005855"><p>delete data</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question522" data-position="6">
            <div class=" clearfix" id="quiz_question-522">

    <h4 class="quiz_question">
        
        Question #5
    </h4>

    <!-- Quiz question Body -->
    <p>A HTTP POST request is to</p>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="522">
                <li class="">

  <input type="radio" name="522" id="522-1509576014214" value="1509576014214" data-quiz-answer-id="1509576014214" data-quiz-question-id="522" disabled="disabled">
  <label for="522-1509576014214"><p>request data</p>
</label>
</li>

                <li class="">

  <input type="radio" name="522" id="522-1509576022270" value="1509576022270" data-quiz-answer-id="1509576022270" data-quiz-question-id="522" disabled="disabled" checked="checked">
  <label for="522-1509576022270"><p>submit data</p>
</label>
</li>

                <li class="">

  <input type="radio" name="522" id="522-1509576026309" value="1509576026309" data-quiz-answer-id="1509576026309" data-quiz-question-id="522" disabled="disabled">
  <label for="522-1509576026309"><p>delete data</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question523" data-position="7">
            <div class=" clearfix" id="quiz_question-523">

    <h4 class="quiz_question">
        
        Question #6
    </h4>

    <!-- Quiz question Body -->
    <p>A DNS A record translates to</p>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="523">
                <li class="">

  <input type="radio" name="523" id="523-1509576088941" value="1509576088941" data-quiz-answer-id="1509576088941" data-quiz-question-id="523" disabled="disabled" checked="checked">
  <label for="523-1509576088941"><p>an IP</p>
</label>
</li>

                <li class="">

  <input type="radio" name="523" id="523-1509576096010" value="1509576096010" data-quiz-answer-id="1509576096010" data-quiz-question-id="523" disabled="disabled">
  <label for="523-1509576096010"><p>a domain</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question524" data-position="8">
            <div class=" clearfix" id="quiz_question-524">

    <h4 class="quiz_question">
        
        Question #7
    </h4>

    <!-- Quiz question Body -->
    <p>A DNS CNAME record translates to</p>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="524">
                <li class="">

  <input type="radio" name="524" id="524-1509576125215" value="1509576125215" data-quiz-answer-id="1509576125215" data-quiz-question-id="524" disabled="disabled">
  <label for="524-1509576125215"><p>an IP</p>
</label>
</li>

                <li class="">

  <input type="radio" name="524" id="524-1509576127919" value="1509576127919" data-quiz-answer-id="1509576127919" data-quiz-question-id="524" disabled="disabled" checked="checked">
  <label for="524-1509576127919"><p>a domain</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question525" data-position="9">
            <div class=" clearfix" id="quiz_question-525">

    <h4 class="quiz_question">
        
        Question #8
    </h4>

    <!-- Quiz question Body -->
    <p>What is TTL within the context of DNS</p>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="525">
                <li class="">

  <input type="radio" name="525" id="525-1509576210064" value="1509576210064" data-quiz-answer-id="1509576210064" data-quiz-question-id="525" disabled="disabled" checked="checked">
  <label for="525-1509576210064"><p>a time period when DNS query results are cached</p>
</label>
</li>

                <li class="">

  <input type="radio" name="525" id="525-1509576228536" value="1509576228536" data-quiz-answer-id="1509576228536" data-quiz-question-id="525" disabled="disabled">
  <label for="525-1509576228536"><p>a time period when DNS is not answering requests</p>
</label>
</li>

                <li class="">

  <input type="radio" name="525" id="525-1509576242638" value="1509576242638" data-quiz-answer-id="1509576242638" data-quiz-question-id="525" disabled="disabled">
  <label for="525-1509576242638"><p>a time period for DNS maintenance</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question526" data-position="10">
            <div class=" clearfix" id="quiz_question-526">

    <h4 class="quiz_question">
        
        Question #9
    </h4>

    <!-- Quiz question Body -->
    <p>Why web servers usually use child processes?</p>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="526">
                <li class="">

  <input type="radio" name="526" id="526-1509588974072" value="1509588974072" data-quiz-answer-id="1509588974072" data-quiz-question-id="526" disabled="disabled">
  <label for="526-1509588974072"><p>That’s just a subjective technical choice from the developers who created the software</p>
</label>
</li>

                <li class="">

  <input type="radio" name="526" id="526-1509588994827" value="1509588994827" data-quiz-answer-id="1509588994827" data-quiz-question-id="526" disabled="disabled" checked="checked">
  <label for="526-1509588994827"><p>So that the web server can dynamically change the number of child process to accommodate the volume of requests to be processed</p>
</label>
</li>

                <li class="">

  <input type="radio" name="526" id="526-1509589023160" value="1509589023160" data-quiz-answer-id="1509589023160" data-quiz-question-id="526" disabled="disabled">
  <label for="526-1509589023160"><p>To prevent memory leak</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>

      </section>
    </div>
  </div>


          <h2 class="gap">
    Your servers
  </h2>

  <div class="panel panel-default overflow_visible">
    <div class="panel-body">
      <table class="table table-striped">
  <thead>
    <tr>
      <th>Name</th>
      <th>Username</th>
      <th>IP</th>
      <th>State</th>
      <th></th>
    </tr>
  </thead>

  <tbody>
      <tr>
        <td>4547-web-01</td>
        <td><code>ubuntu</code></td>
        <td><code>18.209.13.104</code></td>
        <td>running</td>
        <td>
          <div class="btn-group">
            <button type="button" class="btn btn-sm btn-default dropdown-toggle" data-toggle="dropdown">
              Actions
              <span class="caret"></span>
              <span class="sr-only">Toggle Dropdown</span>
            </button>
            <ul class="dropdown-menu dropdown-menu-right">
                <li><a data-confirm="Are you sure to reboot 4547-web-01?" href="/servers/9261/soft_reboot">Soft reboot</a></li>
                  <li><a data-confirm="Are you sure to hard reboot 4547-web-01?" href="/servers/9261/hard_reboot">Hard reboot</a></li>

              <li role="separator" class="divider"></li>

                <li class="dropdown-header">Need a new server? Ask the staff!</li>
            </ul>
          </div>
        </td>
      </tr>
    
  </tbody>
</table>

    </div>
  </div>

          <h2 class="gap">Tasks</h2>

    <div data-role="task1399" data-position="1" id="task-num-0">
      <div class="panel panel-default task-card " id="task-1399">
  <span id="user_id" data-id="4547"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      0. Transfer a file to your server
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="4547"></span>

    <!-- Progress vs Score -->
      <div class="task_progress_score_bar" data-task-id="1399" data-correction-id="376194">
        <div class="task_progress_bar" style="width: 0%;">
          <div class="task_score_bar">
          </div>
        </div>
        <div class="task_progress_score_text">
          Score: <span class="task_score_value">0.00%</span> (<span class="task_progress_value">Checks completed: 0.00%</span>)
        </div>
      </div>

    <!-- Task Body -->
    <p>Write a Bash script that transfers a file from our client to a server:</p>

<p>Requirements:</p>

<ul>
<li>Accepts 4 parameters

<ol>
<li>The path to the file to be transferred</li>
<li>The IP of the server we want to transfer the file to</li>
<li>The username <code>scp</code> connects with</li>
<li>The path to the SSH private key that <code>scp</code> uses</li>
</ol></li>
<li>Display <code>Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY</code> if less than 4 parameters passed</li>
<li><code>scp</code> must transfer the file to the user home directory <code>~/</code></li>
<li>Strict host key checking must be disabled when using <code>scp</code> </li>
</ul>

<p>Example:</p>

<pre><code>sylvain@ubuntu$ ./0-transfer_file
Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY
sylvain@ubuntu$
sylvain@ubuntu$ ssh ubuntu@8.8.8.8 -i /vagrant/sylvain 'ls ~/'
afile
sylvain@ubuntu$ 
sylvain@ubuntu$ touch some_page.html
sylvain@ubuntu$ ./0-transfer_file some_page.html 8.8.8.8 sylvain /vagrant/private_key
some_page.html                                     100%   12     0.1KB/s   00:00
sylvain@ubuntu$ ssh ubuntu@8.8.8.8 -i /vagrant/private_key 'ls ~/'
afile
some_page.html
sylvain@ubuntu$
</code></pre>

<p>In this example, I:</p>

<ul>
<li>remotely execute the <code>ls ~/</code> command via <code>ssh</code> to see what <code>~/</code> contains</li>
<li>create a file named <code>some_page.html</code></li>
<li>execute my <code>0-transfer_file</code> script</li>
<li> remotely execute the <code>ls ~/</code> command via <code>ssh</code> to see that the file <code>some_page.html</code> has been successfully transferred</li>
</ul>

<p>That is one way of publishing your website pages to your server.</p>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-system_engineering-devops</code></li>
            <li>Directory: <code>0x0C-web_server</code></li>
            <li>File: <code>0-transfer_file</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">
        
<div>
    <button class="student_task_done btn btn-default btn-sm no" data-task-id="1399">
      <span class="no"><i aria-hidden="true" class="fa fa-square-o "></i></span>
      <span class="yes"><i aria-hidden="true" class="fa fa-check-square-o "></i></span>
      <span class="pending"><i aria-hidden="true" class="fa fa-spinner  fa-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="1399" data-batch-id="234" data-toggle="modal" data-target="#task-1399-users-done-modal">
    Help
  </button>
  


      <button class="btn btn-default btn-sm" data-task-id="1399" data-toggle="modal" data-target="#task-test-correction-1399-correction-modal" id="task-num-0-check-code-btn">
          Check your code
      </button>
      


      <button class="btn btn-primary btn-sm task_ask_new_correction" data-task-id="1399" data-correction-id="376194">
        Ask for a new correction <span class="in_progress_info">: in progress...</span><span class="error_occurred_info">: an error occurred</span>
      </button>

    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

      <button class="btn btn-default btn-sm" data-task-id="1399" data-toggle="modal" data-target="#task-qa-review-1399-modal">
        QA Review
      </button>
      

</div>


        <div class="fs-4">
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task1400" data-position="2" id="task-num-1">
      <div class="panel panel-default task-card " id="task-1400">
  <span id="user_id" data-id="4547"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      1. Install nginx web server
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="4547"></span>

    <!-- Progress vs Score -->
      <div class="task_progress_score_bar" data-task-id="1400" data-correction-id="376194">
        <div class="task_progress_bar" style="width: 100%;">
          <div class="task_score_bar" style="width: 100%;">
          </div>
        </div>
        <div class="task_progress_score_text">
          Score: <span class="task_score_value">100.00%</span> (<span class="task_progress_value">Checks completed: 100.00%</span>)
        </div>
      </div>

    <!-- Task Body -->
    <p><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/01cab59e881e31842b8d47a0974e8d3b6f0f2001.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220902%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20220902T145216Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=4b1e7700a954147340d3650a0a9c9d08f45bba783f002269e6c640832cb5d644" alt="" loading="lazy" style=""></p>

<p>Readme:</p>

<ul>
<li><a href="/rltoken/qU2tVilKLygFZcRpEWD3lw" title="-y on apt-get command" target="_blank">-y on apt-get command</a></li>
</ul>

<p>Web servers are the piece of software generating and serving HTML pages, let’s install one!</p>

<p>Requirements:</p>

<ul>
<li>Install <code>nginx</code> on your <code>web-01</code> server</li>
<li>Nginx should be listening on port 80</li>
<li>When querying Nginx at its root <code>/</code> with a GET request (requesting a page)  using <code>curl</code>, it must return a page that contains the string <code>Hello World</code></li>
<li>As an answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements (this script will be run on the server itself)</li>
<li>You can’t use <code>systemctl</code> for restarting <code>nginx</code></li>
</ul>

<p>Server terminal:</p>

<pre><code>root@sy-web-01$ ./1-install_nginx_web_server &gt; /dev/null 2&gt;&amp;1
root@sy-web-01$ 
root@sy-web-01$ curl localhost
Hello World!
root@sy-web-01$ 
</code></pre>

<p>Local terminal:</p>

<pre><code>sylvain@ubuntu$ curl 34.198.248.145/
Hello World!
sylvain@ubuntu$ curl -sI 34.198.248.145/
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 21 Feb 2017 23:43:22 GMT
Content-Type: text/html
Content-Length: 30
Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
Connection: keep-alive
ETag: "58abea7c-1e"
Accept-Ranges: bytes

sylvain@ubuntu$
</code></pre>

<p>In this example <code>34.198.248.145</code> is the IP of my <code>web-01</code> server. If you want to query the Nginx that is locally installed on your server, you can use <code>curl 127.0.0.1</code>.</p>

<p>If things are not going as expected, make sure to check out Nginx logs, they can be found in <code>/var/log/</code>.</p>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-system_engineering-devops</code></li>
            <li>Directory: <code>0x0C-web_server</code></li>
            <li>File: <code>1-install_nginx_web_server</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">
        
<div>
    <button class="student_task_done btn btn-default btn-sm yes" data-task-id="1400">
      <span class="no"><i aria-hidden="true" class="fa fa-square-o "></i></span>
      <span class="yes"><i aria-hidden="true" class="fa fa-check-square-o "></i></span>
      <span class="pending"><i aria-hidden="true" class="fa fa-spinner  fa-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="1400" data-batch-id="234" data-toggle="modal" data-target="#task-1400-users-done-modal">
    Help
  </button>
  


      <button class="btn btn-default btn-sm" data-task-id="1400" data-toggle="modal" data-target="#task-test-correction-1400-correction-modal" id="task-num-1-check-code-btn">
          Check your code
      </button>
      



    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

      <button class="btn btn-default btn-sm" data-task-id="1400" data-toggle="modal" data-target="#task-qa-review-1400-modal">
        QA Review
      </button>
      

</div>


        <div class="fs-4">
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task1401" data-position="3" id="task-num-2">
      <div class="panel panel-default task-card " id="task-1401">
  <span id="user_id" data-id="4547"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      2. Setup a domain name
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="4547"></span>

    <!-- Progress vs Score -->
      <div class="task_progress_score_bar" data-task-id="1401" data-correction-id="376194">
        <div class="task_progress_bar" style="width: 50%;">
          <div class="task_score_bar" style="width: 100%;">
          </div>
        </div>
        <div class="task_progress_score_text">
          Score: <span class="task_score_value">50.00%</span> (<span class="task_progress_value">Checks completed: 50.00%</span>)
        </div>
      </div>

    <!-- Task Body -->
    <p><a href="/rltoken/yRrwiHrS15iQQZku72p0aQ" title=".TECH Domains" target="_blank">.TECH Domains</a> is one of the top domain providers. They are known for the stability and quality of their DNS hosting solution. We partnered with .TECH Domains so that you can learn about DNS.</p>

<p>.TECH Domains worked with domain name registrars to give you access to a free domain name for a year. Please get the promo code in your <a href="/rltoken/b-Y81kiPBFJ_6wxJaSmBgQ" title="tools space" target="_blank">tools space</a>. Feel free to drop a thank you tweet for <a href="/rltoken/d9XjYlM-CqTRHJEcaKpcVQ" title=".TECH Domains" target="_blank">.TECH Domains</a>.</p>

<p>Provide the domain name in your answer file.</p>

<p>Requirement:</p>

<ul>
<li>provide the domain name only (example: <code>foobar.tech</code>), no subdomain (example: <code>www.foobar.tech</code>)</li>
<li>configure your DNS records with an A entry so that your root domain points to your <code>web-01</code> IP address <strong>Warning: the propagation of your records can take time (~1-2 hours)</strong></li>
<li>go to <a href="/rltoken/7s2XnwohTKBNE8c_ibAt4g" title="your profile" target="_blank">your profile</a> and enter your domain in the <code>Project website url</code> field

<ul>
<li>when creating the account, if you live in <code>France</code>, select <code>France</code> as country not <code>France metropolitaine</code>.</li>
</ul></li>
</ul>

<p>Example:</p>

<pre><code>sylvain@ubuntu$ cat 2-setup_a_domain_name
myschool.tech
sylvain@ubuntu$
sylvain@ubuntu$ dig myschool.tech

; &lt;&lt;&gt;&gt; DiG 9.10.6 &lt;&lt;&gt;&gt; myschool.tech
;; global options: +cmd
;; Got answer:
;; -&gt;&gt;HEADER&lt;&lt;- opcode: QUERY, status: NOERROR, id: 26785
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 512
;; QUESTION SECTION:
;myschool.tech.     IN  A

;; ANSWER SECTION:
myschool.tech.  7199    IN  A   184.72.193.201

;; Query time: 65 msec
;; SERVER: 8.8.8.8#53(8.8.8.8)
;; WHEN: Fri Aug 02 09:44:36 PDT 2019
;; MSG SIZE  rcvd: 65

sylvain@ubuntu$
</code></pre>

<p>When your domain name is setup, please verify the Registrar here: <a href="/rltoken/s8vsjayVUHJza59GXtuzpw" title="https://whois.whoisxmlapi.com/" target="_blank">https://whois.whoisxmlapi.com/</a>  and you must see in the JSON response: <code>"registrarName": "Dotserve Inc"</code></p>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-system_engineering-devops</code></li>
            <li>Directory: <code>0x0C-web_server</code></li>
            <li>File: <code>2-setup_a_domain_name</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">
        
<div>
    <button class="student_task_done btn btn-default btn-sm no" data-task-id="1401">
      <span class="no"><i aria-hidden="true" class="fa fa-square-o "></i></span>
      <span class="yes"><i aria-hidden="true" class="fa fa-check-square-o "></i></span>
      <span class="pending"><i aria-hidden="true" class="fa fa-spinner  fa-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="1401" data-batch-id="234" data-toggle="modal" data-target="#task-1401-users-done-modal">
    Help
  </button>
  


      <button class="btn btn-default btn-sm" data-task-id="1401" data-toggle="modal" data-target="#task-test-correction-1401-correction-modal" id="task-num-2-check-code-btn">
          Check your code
      </button>
      


      <button class="btn btn-primary btn-sm task_ask_new_correction" data-task-id="1401" data-correction-id="376194">
        Ask for a new correction <span class="in_progress_info">: in progress...</span><span class="error_occurred_info">: an error occurred</span>
      </button>

    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

      <button class="btn btn-default btn-sm" data-task-id="1401" data-toggle="modal" data-target="#task-qa-review-1401-modal">
        QA Review
      </button>
      

</div>


        <div class="fs-4">
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task1402" data-position="4" id="task-num-3">
      <div class="panel panel-default task-card " id="task-1402">
  <span id="user_id" data-id="4547"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      3. Redirection
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="4547"></span>

    <!-- Progress vs Score -->
      <div class="task_progress_score_bar" data-task-id="1402" data-correction-id="376194">
        <div class="task_progress_bar" style="width: 66.6667%;">
          <div class="task_score_bar" style="width: 100%;">
          </div>
        </div>
        <div class="task_progress_score_text">
          Score: <span class="task_score_value">66.67%</span> (<span class="task_progress_value">Checks completed: 66.67%</span>)
        </div>
      </div>

    <!-- Task Body -->
    <p>Readme:</p>

<ul>
<li><a href="/rltoken/Afg1zCifjmIygL1se0ghhg" title="Replace a line with multiple lines with sed" target="_blank">Replace a line with multiple lines with sed</a></li>
</ul>

<p>Configure your Nginx server so that <code>/redirect_me</code> is redirecting to another page.</p>

<p>Requirements:</p>

<ul>
<li>The redirection must be a “301 Moved Permanently”</li>
<li>You answer file should be a Bash script containing commands to automatically configure a Ubuntu machine to respect above requirements</li>
<li>Using what you did with <code>1-install_nginx_web_server</code>, write <code>3-redirection</code> so that it configures a brand new Ubuntu machine to the requirements asked in this task</li>
</ul>

<p>Example:</p>

<pre><code>sylvain@ubuntu$ curl -sI 34.198.248.145/redirect_me/
HTTP/1.1 301 Moved Permanently
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 21 Feb 2017 21:36:04 GMT
Content-Type: text/html
Content-Length: 193
Connection: keep-alive
Location: https://www.youtube.com/watch?v=QH2-TGUlwu4

sylvain@ubuntu$
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-system_engineering-devops</code></li>
            <li>Directory: <code>0x0C-web_server</code></li>
            <li>File: <code>3-redirection</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">
        
<div>
    <button class="student_task_done btn btn-default btn-sm yes" data-task-id="1402">
      <span class="no"><i aria-hidden="true" class="fa fa-square-o "></i></span>
      <span class="yes"><i aria-hidden="true" class="fa fa-check-square-o "></i></span>
      <span class="pending"><i aria-hidden="true" class="fa fa-spinner  fa-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="1402" data-batch-id="234" data-toggle="modal" data-target="#task-1402-users-done-modal">
    Help
  </button>
  


      <button class="btn btn-default btn-sm" data-task-id="1402" data-toggle="modal" data-target="#task-test-correction-1402-correction-modal" id="task-num-3-check-code-btn">
          Check your code
      </button>
      


      <button class="btn btn-primary btn-sm task_ask_new_correction" data-task-id="1402" data-correction-id="376194">
        Ask for a new correction <span class="in_progress_info">: in progress...</span><span class="error_occurred_info">: an error occurred</span>
      </button>

    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

      <button class="btn btn-default btn-sm" data-task-id="1402" data-toggle="modal" data-target="#task-qa-review-1402-modal">
        QA Review
      </button>
      

</div>


        <div class="fs-4">
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task1403" data-position="5" id="task-num-4">
      <div class="panel panel-default task-card " id="task-1403">
  <span id="user_id" data-id="4547"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      4. Not found page 404
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="4547"></span>

    <!-- Progress vs Score -->
      <div class="task_progress_score_bar" data-task-id="1403" data-correction-id="376194">
        <div class="task_progress_bar" style="width: 100%;">
          <div class="task_score_bar" style="width: 100%;">
          </div>
        </div>
        <div class="task_progress_score_text">
          Score: <span class="task_score_value">100.00%</span> (<span class="task_progress_value">Checks completed: 100.00%</span>)
        </div>
      </div>

    <!-- Task Body -->
    <p>Configure your Nginx server to have a custom 404 page that contains the string <code>Ceci n'est pas une page</code>.</p>

<p>Requirements:</p>

<ul>
<li>The page must return an HTTP 404 error code</li>
<li>The page must contain the string <code>Ceci n'est pas une page</code></li>
<li>Using what you did with <code>3-redirection</code>, write <code>4-not_found_page_404</code> so that it configures a brand new Ubuntu machine to the requirements asked in this task</li>
</ul>

<p>Example:</p>

<pre><code>sylvain@ubuntu$ curl -sI 34.198.248.145/xyz
HTTP/1.1 404 Not Found
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 21 Feb 2017 21:46:43 GMT
Content-Type: text/html
Content-Length: 26
Connection: keep-alive
ETag: "58acb50e-1a"

sylvain@ubuntu$ curl 34.198.248.145/xyzfoo
Ceci n'est pas une page

sylvain@ubuntu$
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-system_engineering-devops</code></li>
            <li>Directory: <code>0x0C-web_server</code></li>
            <li>File: <code>4-not_found_page_404</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">
        
<div>
    <button class="student_task_done btn btn-default btn-sm yes" data-task-id="1403">
      <span class="no"><i aria-hidden="true" class="fa fa-square-o "></i></span>
      <span class="yes"><i aria-hidden="true" class="fa fa-check-square-o "></i></span>
      <span class="pending"><i aria-hidden="true" class="fa fa-spinner  fa-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="1403" data-batch-id="234" data-toggle="modal" data-target="#task-1403-users-done-modal">
    Help
  </button>
  


      <button class="btn btn-default btn-sm" data-task-id="1403" data-toggle="modal" data-target="#task-test-correction-1403-correction-modal" id="task-num-4-check-code-btn">
          Check your code
      </button>
      



    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

      <button class="btn btn-default btn-sm" data-task-id="1403" data-toggle="modal" data-target="#task-qa-review-1403-modal">
        QA Review
      </button>
      

</div>


        <div class="fs-4">
        </div>
      </div>


  </div>
</div>

    </div>

    <p class="lg-gap">
      <a class="btn btn-primary btn-block" data-confirm="Are you sure? Make sure you focused on the mandatory tasks first" href="/projects/266/unlock_optionals">Done with the mandatory tasks? Unlock 2 advanced tasks now!</a>
    </p>



          <div data-react-class="projects/ProjectReadyForReview" data-react-props="{&quot;csrfToken&quot;:&quot;y6Yb0hdf3szcFxlao5rnd7WEg30WZDyVKlNiW_z9OBs3Qd4tZCTgbJb00QUyCQGDE54bdg1Ya3QQJGQLUBmVeQ&quot;,&quot;firstReview&quot;:false,&quot;peerReview&quot;:{&quot;availableReviewersURI&quot;:&quot;/corrections/376194/available_reviewers.json&quot;,&quot;canReviewPeerDirectly&quot;:true,&quot;correctCorrectionURI&quot;:&quot;https://intranet.hbtn.io/corrections/376194/correct&quot;,&quot;qaReviewsURI&quot;:&quot;/corrections/to_review&quot;,&quot;readyForReviewURI&quot;:&quot;/corrections/376194/toggle_ready_for_review.json&quot;,&quot;reviewDeadline&quot;:&quot;2022-08-31T00:00:00.000-05:00&quot;,&quot;synchronousManualReview&quot;:false},&quot;toggled&quot;:false}" data-react-cache-id="projects/ProjectReadyForReview-0"><div class="row gap"><div class="col-md-12"><div class="text-center"><button class="btn btn-lg btn-primary">Ready for a new manual review</button></div></div></div></div>

          

  </div>