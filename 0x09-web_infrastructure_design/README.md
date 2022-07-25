<div class="col-xs-12 col-md-10 col-lg-8 contains-images">

      <h1 class="gap">0x09. Web infrastructure design</h1>

  <div data-react-class="tags/Tags" data-react-props="{&quot;tags&quot;:[]}" data-react-cache-id="tags/Tags-0"></div>

  <ul class="list-group metadata" id="project-metadata">

    <li class="list-group-item">
      <i aria-hidden="true" class="fa fa-user  fa-fw"></i>
      By Sylvain Kalache, co-founder at Holberton School
    </li>

    <li class="list-group-item">
      <i aria-hidden="true" class="fa fa-cogs  fa-fw"></i>
      Weight: 1
    </li>



    <li class="list-group-item">
      <i aria-hidden="true" class="fa fa-users  fa-fw"></i>
      Project to be done in teams of 3 people
    </li>


      <li class="list-group-item">
        <i aria-hidden="true" class="fa fa-calendar  fa-fw"></i>
          Ongoing second chance project - started <div data-react-class="common/DateTime" data-react-props="{&quot;showDate&quot;:true,&quot;showTime&quot;:false,&quot;value&quot;:&quot;2022-07-19T00:00:00.000-05:00&quot;}" data-react-cache-id="common/DateTime-0" class="d-inline-block"><span data-container="body" data-html="false" data-placement="auto top" data-toggle="tooltip" title="" data-original-title="2022-07-19 00:00 (GMT-05:00)"><span class="datetime">Jul 19, 2022 </span></span></div>, must end by <div data-react-class="common/DateTime" data-react-props="{&quot;showDate&quot;:true,&quot;showTime&quot;:false,&quot;value&quot;:&quot;2022-07-28T00:00:00.000-05:00&quot;}" data-react-cache-id="common/DateTime-0" class="d-inline-block"><span data-container="body" data-html="false" data-placement="auto top" data-toggle="tooltip" title="" data-original-title="2022-07-28 00:00 (GMT-05:00)"><span class="datetime">Jul 28, 2022 </span></span></div>
          - you're done with <span id="student_task_done_percentage">100</span>% of tasks.
      </li>


      <li class="list-group-item">
        <i aria-hidden="true" class="fa fa-check-square  fa-fw"></i>
          <strong>Manual QA review must be done</strong>
          (request it when you are done with the project)
      </li>



</ul>




    <div id="project_id" style="display: none" data-project-id="302"></div>



      

        <div class="panel panel-default">
    <div class="panel-heading">
      <h3 class="panel-title">Concepts</h3>
    </div>
    <div class="panel-body">
      <p>
        <em>For this project, we expect you to look at these concepts:</em>
      </p>

      <ul>
          <li>
            <a href="/concepts/12">DNS</a>
          </li>
          <li>
            <a href="/concepts/13">Monitoring</a>
          </li>
          <li>
            <a href="/concepts/17">Web Server</a>
          </li>
          <li>
            <a href="/concepts/33">Network basics</a>
          </li>
          <li>
            <a href="/concepts/46">Load balancer</a>
          </li>
          <li>
            <a href="/concepts/67">Server</a>
          </li>
      </ul>
    </div>
  </div>


      <div class="panel panel-default" id="project-description">
  <div class="panel-body">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/lQNEW76KdYg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""></iframe>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><strong>Network basics</strong> concept page</li>
<li><strong>Server</strong> concept page</li>
<li><strong>Web server</strong> concept page</li>
<li><strong>DNS</strong> concept page</li>
<li><strong>Load balancer</strong> concept page</li>
<li><strong>Monitoring</strong> concept page</li>
<li><a href="/rltoken/woDFYUG0y_SrA79AaYbFCA" title="What is a database" target="_blank">What is a database</a> </li>
<li><a href="/rltoken/Nb8B47Y2D8SLqQMOKVoQyQ" title="What's the difference between a web server and an app server?" target="_blank">What’s the difference between a web server and an app server?</a></li>
<li><a href="/rltoken/ojwHUACZEtIWfI9M6i7c3g" title="DNS record types" target="_blank">DNS record types</a> </li>
<li><a href="/rltoken/wYpewVpIp9PSqqL27RPafg" title="Single point of failure" target="_blank">Single point of failure</a> </li>
<li><a href="/rltoken/Mlvynt0OgLQXrxjrC5Wlnw" title="How to avoid downtime when deploying new code" target="_blank">How to avoid downtime when deploying new code</a> </li>
<li><a href="/rltoken/POX3jE0S6TChQHSYQraYeQ" title="High availability cluster (active-active/active-passive)" target="_blank">High availability cluster (active-active/active-passive)</a> </li>
<li><a href="/rltoken/N4BwU4wYDNW02kdzMiekFw" title="What is HTTPS" target="_blank">What is HTTPS</a> </li>
<li><a href="/rltoken/ZFTutaKN4wWzmL4fWhQmeg" title="What is a firewall" target="_blank">What is a firewall</a> </li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/Dvn7v5U404zIccrJ_jDevg" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>You must be able to draw a diagram covering the web stack you built with the sysadmin/devops track projects</li>
<li>You must be able to explain what each component is doing</li>
<li>You must be able to explain system redundancy</li>
<li>Know all the mentioned acronyms: LAMP, SPOF, QPS</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>For each task, once you are done whiteboarding (on a whiteboard, piece of paper or software or your choice), take a picture/screenshot of your diagram</li>
<li>This project will be manually reviewed:</li>
<li>As each task is completed, the name of that task will turn green</li>
<li>Upload a screenshot, showing that you completed the required levels, to any image hosting service (I personally use <a href="/rltoken/QorG0rvw1PzqWBVrqWW6Sg" title="imgur" target="_blank">imgur</a> but feel free to use anything you want). </li>
<li>For the following tasks, insert the link from of your screenshot into the answer file </li>
<li>After pushing your answer file to GitHub, insert the GitHub file link into the URL box</li>
<li>You will also have to whiteboard each task in front of a mentor, staff or student - no computer or notes will be allowed during the whiteboarding session</li>
<li>Focus on what you are being asked: </li>
<li>Cover what the requirements mention, we will explore details in a later project</li>
<li>Keep in mind that you will have 30 minutes to perform the exercise, you will get points for what is asked in requirements</li>
<li>Similarly in a job interview, you should answer what the interviewer asked for, be careful about being too verbose - always ask the interviewer if going into details is necessary - speaking too much can play against you</li>
<li>In this project, again, avoid going in details if not asked</li>
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
          <div class="quiz_question_item_container" data-role="quiz_question196" data-position="1">
            <div class=" clearfix" id="quiz_question-196">

    <h4 class="quiz_question">
        
        Question #0
    </h4>

    <!-- Quiz question Body -->
    <p>What is a server?</p>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="196">
                <li class="">
  <input type="checkbox" name="quiz-answer-1500349599150" id="quiz-answer-1500349599150" data-quiz-question-id="196" data-quiz-answer-id="1500349599150" disabled="disabled" checked="checked">
  <label for="quiz-answer-1500349599150">
    <p>A server is a device, a virtual device or computer program or providing functionality for other programs or devices, called “clients”.</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1500349781028" id="quiz-answer-1500349781028" data-quiz-question-id="196" data-quiz-answer-id="1500349781028" disabled="disabled">
  <label for="quiz-answer-1500349781028">
    <p>A server is a software that serves web pages.</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1500349815591" id="quiz-answer-1500349815591" data-quiz-question-id="196" data-quiz-answer-id="1500349815591" disabled="disabled">
  <label for="quiz-answer-1500349815591">
    <p>A server is returning information to other computers when asked.</p>

</label></li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question197" data-position="2">
            <div class=" clearfix" id="quiz_question-197">

    <h4 class="quiz_question">
        
        Question #1
    </h4>

    <!-- Quiz question Body -->
    <p>What is a web server?</p>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="197">
                <li class="">
  <input type="checkbox" name="quiz-answer-1500349941412" id="quiz-answer-1500349941412" data-quiz-question-id="197" data-quiz-answer-id="1500349941412" disabled="disabled">
  <label for="quiz-answer-1500349941412">
    <p>A web server is a software or physical device serving web pages over HTTP.</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1500350010977" id="quiz-answer-1500350010977" data-quiz-question-id="197" data-quiz-answer-id="1500350010977" disabled="disabled" checked="checked">
  <label for="quiz-answer-1500350010977">
    <p>A web server is a software that serves web pages to clients upon their request, it does this over the protocol HTTP.</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1500350065816" id="quiz-answer-1500350065816" data-quiz-question-id="197" data-quiz-answer-id="1500350065816" disabled="disabled">
  <label for="quiz-answer-1500350065816">
    <p>A web server is a software that serves web pages to clients upon their request.</p>

</label></li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question198" data-position="3">
            <div class=" clearfix" id="quiz_question-198">

    <h4 class="quiz_question">
        
        Question #2
    </h4>

    <!-- Quiz question Body -->
    <p>What is a codebase?</p>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="198">
                <li class="">
  <input type="checkbox" name="quiz-answer-1500350227244" id="quiz-answer-1500350227244" data-quiz-question-id="198" data-quiz-answer-id="1500350227244" disabled="disabled">
  <label for="quiz-answer-1500350227244">
    <p>A list of software libraries.</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1500350237695" id="quiz-answer-1500350237695" data-quiz-question-id="198" data-quiz-answer-id="1500350237695" disabled="disabled" checked="checked">
  <label for="quiz-answer-1500350237695">
    <p>Is the collection of source code that is used to build a software system.</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1500350292432" id="quiz-answer-1500350292432" data-quiz-question-id="198" data-quiz-answer-id="1500350292432" disabled="disabled">
  <label for="quiz-answer-1500350292432">
    <p>Is the most important files of a software system.</p>

</label></li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question199" data-position="4">
            <div class=" clearfix" id="quiz_question-199">

    <h4 class="quiz_question">
        
        Question #3
    </h4>

    <!-- Quiz question Body -->
    <p>What is a database?</p>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="199">
                <li class="">
  <input type="checkbox" name="quiz-answer-1500350320243" id="quiz-answer-1500350320243" data-quiz-question-id="199" data-quiz-answer-id="1500350320243" disabled="disabled">
  <label for="quiz-answer-1500350320243">
    <p>Is a collection of text files that are stored so that it can be easily accessed, updated and managed by the local application.</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1500350354211" id="quiz-answer-1500350354211" data-quiz-question-id="199" data-quiz-answer-id="1500350354211" disabled="disabled">
  <label for="quiz-answer-1500350354211">
    <p>Is a collection of information that is stored on a physical server and organized so that it can be easily accessed, updated and managed.</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1500350380872" id="quiz-answer-1500350380872" data-quiz-question-id="199" data-quiz-answer-id="1500350380872" disabled="disabled" checked="checked">
  <label for="quiz-answer-1500350380872">
    <p>Is a collection of information that is stored and organized so that it can be easily accessed, updated and managed.</p>

</label></li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question200" data-position="5">
            <div class=" clearfix" id="quiz_question-200">

    <h4 class="quiz_question">
        
        Question #4
    </h4>

    <!-- Quiz question Body -->
    <p>What is a DNS?</p>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="200">
                <li class="">
  <input type="checkbox" name="quiz-answer-1500350778981" id="quiz-answer-1500350778981" data-quiz-question-id="200" data-quiz-answer-id="1500350778981" disabled="disabled">
  <label for="quiz-answer-1500350778981">
    <p>A list of domain names.</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1500350859301" id="quiz-answer-1500350859301" data-quiz-question-id="200" data-quiz-answer-id="1500350859301" disabled="disabled" checked="checked">
  <label for="quiz-answer-1500350859301">
    <p>A system to translate domain names into IP addresses.</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1500350921490" id="quiz-answer-1500350921490" data-quiz-question-id="200" data-quiz-answer-id="1500350921490" disabled="disabled">
  <label for="quiz-answer-1500350921490">
    <p>A system that contain all Internet IPs.</p>

</label></li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question201" data-position="6">
            <div class=" clearfix" id="quiz_question-201">

    <h4 class="quiz_question">
        
        Question #5
    </h4>

    <!-- Quiz question Body -->
    <p>What is HTTPS?</p>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="201">
                <li class="">
  <input type="checkbox" name="quiz-answer-1500351759727" id="quiz-answer-1500351759727" data-quiz-question-id="201" data-quiz-answer-id="1500351759727" disabled="disabled">
  <label for="quiz-answer-1500351759727">
    <p>A faster version of HTTP.</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1500351766668" id="quiz-answer-1500351766668" data-quiz-question-id="201" data-quiz-answer-id="1500351766668" disabled="disabled">
  <label for="quiz-answer-1500351766668">
    <p>A version of HTTP that protect your personal information.</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1500351799721" id="quiz-answer-1500351799721" data-quiz-question-id="201" data-quiz-answer-id="1500351799721" disabled="disabled" checked="checked">
  <label for="quiz-answer-1500351799721">
    <p>A version of HTTP that secure the traffic between your browser and the website by encrypting it.</p>

</label></li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question202" data-position="7">
            <div class=" clearfix" id="quiz_question-202">

    <h4 class="quiz_question">
        
        Question #6
    </h4>

    <!-- Quiz question Body -->
    <p>What is TCP/IP?</p>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="202">
                <li class="">
  <input type="checkbox" name="quiz-answer-1500352214568" id="quiz-answer-1500352214568" data-quiz-question-id="202" data-quiz-answer-id="1500352214568" disabled="disabled" checked="checked">
  <label for="quiz-answer-1500352214568">
    <p>Transmission Control Protocol/Internet Protocol, is a suite of communications protocols used to interconnect network devices on the Internet or any private network.</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1500352236564" id="quiz-answer-1500352236564" data-quiz-question-id="202" data-quiz-answer-id="1500352236564" disabled="disabled">
  <label for="quiz-answer-1500352236564">
    <p>Transmission Control Protocol/Internet Protocol, is a suite of communications protocols used to interconnect network devices on the Internet.</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1500352243387" id="quiz-answer-1500352243387" data-quiz-question-id="202" data-quiz-answer-id="1500352243387" disabled="disabled">
  <label for="quiz-answer-1500352243387">
    <p>Transmission Control Protocol/Internet Protocol, is a suite of communications protocols used to interconnect network devices on private network.</p>

</label></li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>

      </section>
    </div>
  </div>


        
          <h2 class="gap">Tasks</h2>

    <div data-role="task1754" data-position="1" id="task-num-0">
      <div class="panel panel-default task-card " id="task-1754">
  <span id="user_id" data-id="4547"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      0. Simple web stack
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

    <!-- Task Body -->
    <p>A lot of websites are powered by simple web infrastructure, a lot of time it is composed of a single server with a <a href="/rltoken/lBFrw_pTU3_sMuYFptFFsw" title="LAMP stack" target="_blank">LAMP stack</a>.</p>

<p>On a whiteboard, design a one server web infrastructure that hosts the website that is reachable via <code>www.foobar.com</code>. Start your explanation by having a user wanting to access your website.</p>

<p>Requirements:</p>

<ul>
<li> You must use:

<ul>
<li>1 server</li>
<li>1 web server (Nginx)</li>
<li>1 application server</li>
<li>1 application files (your code base)</li>
<li>1 database (MySQL)</li>
<li>1 domain name <code>foobar.com</code> configured with a <code>www</code> record that points to your server IP <code>8.8.8.8</code></li>
</ul></li>
<li>You must be able to explain some specifics about this infrastructure:

<ul>
<li>What is a server</li>
<li>What is the role of the domain name</li>
<li>What type of DNS record <code>www</code> is in <code>www.foobar.com</code></li>
<li>What is the role of the web server</li>
<li>What is the role of the application server</li>
<li>What is the role of the database</li>
<li>What is the server using to communicate with the computer of the user requesting the website</li>
</ul></li>
<li>You must be able to explain what the issues are with this infrastructure:

<ul>
<li>SPOF</li>
<li>Downtime when maintenance needed (like deploying new code web server needs to be restarted)</li>
<li>Cannot scale if too much incoming traffic</li>
</ul></li>
</ul>

<p>Please, remember that everything must be written in English to further your technical ability in a variety of settings.</p>

  </div>

  <div class="list-group">
    <!-- Task URLs -->
      <div class="list-group-item">
        <div class="blog_post_div">
          <h4>Add URLs here:</h4>

          <div class="input-group">
            <input id="input_1754" type="text" value="" class="form-control">
            <span class="input-group-btn">
              <button data-task-requesting="0" data-user-id="4547" data-task-id="1754" type="button" class="add_task_url btn btn-primary">
                Save
              </button>
            </span>
          </div>

          <div class="task_url_error_msg" data-task-id="1754"></div>

          <ol class="list_1754 sm-gap">
              <li>
                <a target="_blank" href="https://imgur.com/a/a4BpNzt">https://imgur.com/a/a4BpNzt</a>
                <button data-task-requesting="0" id="1754" type="button" data-task-id="1754" data-task-url-id="58786" class="remove_blog_post btn btn-xs btn-default ml-2">
                  Remove
                </button>
              </li>
          </ol>

        </div>
      </div>

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-system_engineering-devops</code></li>
            <li>Directory: <code>0x09-web_infrastructure_design</code></li>
            <li>File: <code>0-simple_web_stack</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">
        
<div>
    <button class="student_task_done btn btn-default btn-sm yes" data-task-id="1754">
      <span class="no"><i aria-hidden="true" class="fa fa-square-o "></i></span>
      <span class="yes"><i aria-hidden="true" class="fa fa-check-square-o "></i></span>
      <span class="pending"><i aria-hidden="true" class="fa fa-spinner  fa-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

    <button class="users_done_for_task btn btn-default btn-sm" data-task-id="1754" data-project-id="302" data-toggle="modal" data-target="#task-1754-users-done-modal">
      Help
    </button>
    <div class="modal fade users-done-modal" id="task-1754-users-done-modal" data-task-id="1754" data-project-id="302">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "0. Simple web stack"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


</div>


        <div class="fs-4">
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task1755" data-position="2" id="task-num-1">
      <div class="panel panel-default task-card " id="task-1755">
  <span id="user_id" data-id="4547"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      1. Distributed web infrastructure
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

    <!-- Task Body -->
    <p>On a whiteboard, design a three server web infrastructure that hosts the website <code>www.foobar.com</code>.</p>

<p>Requirements:</p>

<ul>
<li> You must add:

<ul>
<li>2 servers</li>
<li>1 web server (Nginx)</li>
<li>1 application server</li>
<li>1 load-balancer (HAproxy)</li>
<li>1 set of application files (your code base)</li>
<li>1 database (MySQL)</li>
</ul></li>
<li>You must be able to explain some specifics about this infrastructure:

<ul>
<li>For every additional element, why you are adding it</li>
<li>What distribution algorithm your load balancer is configured with and how it works</li>
<li>Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both</li>
<li>How a database Primary-Replica (Master-Slave) cluster works</li>
<li>What is the difference between the Primary node and the Replica node in regard to the application</li>
</ul></li>
<li>You must be able to explain what the issues are with this infrastructure:

<ul>
<li>Where are SPOF</li>
<li>Security issues (no firewall, no HTTPS)</li>
<li>No monitoring</li>
</ul></li>
</ul>

<p>Please, remember that everything must be written in English to further your technical ability in a variety of settings.</p>

  </div>

  <div class="list-group">
    <!-- Task URLs -->
      <div class="list-group-item">
        <div class="blog_post_div">
          <h4>Add URLs here:</h4>

          <div class="input-group">
            <input id="input_1755" type="text" value="" class="form-control">
            <span class="input-group-btn">
              <button data-task-requesting="0" data-user-id="4547" data-task-id="1755" type="button" class="add_task_url btn btn-primary">
                Save
              </button>
            </span>
          </div>

          <div class="task_url_error_msg" data-task-id="1755"></div>

          <ol class="list_1755 sm-gap">
              <li>
                <a target="_blank" href="https://imgur.com/a/lkIssr8">https://imgur.com/a/lkIssr8</a>
                <button data-task-requesting="0" id="1755" type="button" data-task-id="1755" data-task-url-id="58789" class="remove_blog_post btn btn-xs btn-default ml-2">
                  Remove
                </button>
              </li>
          </ol>

        </div>
      </div>

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-system_engineering-devops</code></li>
            <li>Directory: <code>0x09-web_infrastructure_design</code></li>
            <li>File: <code>1-distributed_web_infrastructure</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">
        
<div>
    <button class="student_task_done btn btn-default btn-sm yes" data-task-id="1755">
      <span class="no"><i aria-hidden="true" class="fa fa-square-o "></i></span>
      <span class="yes"><i aria-hidden="true" class="fa fa-check-square-o "></i></span>
      <span class="pending"><i aria-hidden="true" class="fa fa-spinner  fa-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

    <button class="users_done_for_task btn btn-default btn-sm" data-task-id="1755" data-project-id="302" data-toggle="modal" data-target="#task-1755-users-done-modal">
      Help
    </button>
    <div class="modal fade users-done-modal" id="task-1755-users-done-modal" data-task-id="1755" data-project-id="302">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "1. Distributed web infrastructure"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


</div>


        <div class="fs-4">
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task1756" data-position="3" id="task-num-2">
      <div class="panel panel-default task-card " id="task-1756">
  <span id="user_id" data-id="4547"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      2. Secured and monitored web infrastructure
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

    <!-- Task Body -->
    <p>On a whiteboard, design a three server web infrastructure that hosts the website <code>www.foobar.com</code>, it must be secured, serve encrypted traffic, and be monitored.</p>

<p>Requirements:</p>

<ul>
<li> You must add:

<ul>
<li>3 firewalls </li>
<li>1 SSL certificate to serve <code>www.foobar.com</code> over HTTPS</li>
<li>3 monitoring clients (data collector for Sumologic or other monitoring services)</li>
</ul></li>
<li>You must be able to explain some specifics about this infrastructure:

<ul>
<li>For every additional element, why you are adding it</li>
<li>What are firewalls for</li>
<li>Why is the traffic served over HTTPS</li>
<li>What monitoring is used for</li>
<li>How the monitoring tool is collecting data</li>
<li>Explain what to do if you want to monitor your web server QPS</li>
</ul></li>
<li>You must be able to explain what the issues are with this infrastructure:

<ul>
<li>Why terminating SSL at the load balancer level is an issue</li>
<li>Why having only one MySQL server capable of accepting writes is an issue</li>
<li>Why having servers with all the same components (database, web server and application server) might be a problem</li>
</ul></li>
</ul>

<p>Please, remember that everything must be written in English to further your technical ability in a variety of settings.</p>

  </div>

  <div class="list-group">
    <!-- Task URLs -->
      <div class="list-group-item">
        <div class="blog_post_div">
          <h4>Add URLs here:</h4>

          <div class="input-group">
            <input id="input_1756" type="text" value="" class="form-control">
            <span class="input-group-btn">
              <button data-task-requesting="0" data-user-id="4547" data-task-id="1756" type="button" class="add_task_url btn btn-primary">
                Save
              </button>
            </span>
          </div>

          <div class="task_url_error_msg" data-task-id="1756"></div>

          <ol class="list_1756 sm-gap">
              <li>
                <a target="_blank" href="https://imgur.com/a/4nGg6z8">https://imgur.com/a/4nGg6z8</a>
                <button data-task-requesting="0" id="1756" type="button" data-task-id="1756" data-task-url-id="58922" class="remove_blog_post btn btn-xs btn-default ml-2">
                  Remove
                </button>
              </li>
          </ol>

        </div>
      </div>

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-system_engineering-devops</code></li>
            <li>Directory: <code>0x09-web_infrastructure_design</code></li>
            <li>File: <code>2-secured_and_monitored_web_infrastructure</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">
        
<div>
    <button class="student_task_done btn btn-default btn-sm yes" data-task-id="1756">
      <span class="no"><i aria-hidden="true" class="fa fa-square-o "></i></span>
      <span class="yes"><i aria-hidden="true" class="fa fa-check-square-o "></i></span>
      <span class="pending"><i aria-hidden="true" class="fa fa-spinner  fa-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

    <button class="users_done_for_task btn btn-default btn-sm" data-task-id="1756" data-project-id="302" data-toggle="modal" data-target="#task-1756-users-done-modal">
      Help
    </button>
    <div class="modal fade users-done-modal" id="task-1756-users-done-modal" data-task-id="1756" data-project-id="302">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "2. Secured and monitored web infrastructure"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


</div>


        <div class="fs-4">
        </div>
      </div>


  </div>
</div>

    </div>

    <p class="lg-gap">
      <a class="btn btn-primary btn-block" data-confirm="Are you sure? Make sure you focused on the mandatory tasks first" href="/projects/302/unlock_optionals">Done with the mandatory tasks? Unlock 1 advanced task now!</a>
    </p>



          <div data-react-class="projects/ProjectReadyForReview" data-react-props="{&quot;availableReviewersURI&quot;:&quot;/corrections/364239/available_reviewers.json&quot;,&quot;canReviewPeerDirectly&quot;:true,&quot;correctCorrectionURI&quot;:&quot;https://intranet.hbtn.io/corrections/364239/correct&quot;,&quot;csrfToken&quot;:&quot;bFCH6lkuF5nJEVPAohmOkWE3c7nQUWbha8YBNQx2n-uQt0IVKlUpOYPym58zimhlxy3rssttMQBRsQdloJIyiQ&quot;,&quot;firstReview&quot;:true,&quot;qaReviewsURI&quot;:&quot;/corrections/to_review&quot;,&quot;readyForReviewURI&quot;:&quot;/corrections/364239/toggle_ready_for_review.json&quot;,&quot;reviewDeadline&quot;:&quot;2022-07-30T00:00:00.000-05:00&quot;,&quot;synchronousManualReview&quot;:false,&quot;toggled&quot;:true}" data-react-cache-id="projects/ProjectReadyForReview-0"><div class="row gap"><div class="col-md-12"><div class="panel panel-default"><div class="panel-heading"><h3 class="panel-title">Ready for manual review</h3></div><div class="panel-body"><p>Now that you are ready to be reviewed, share your link to your peers.</p><div class="input-group my-2"><span class="form-control user-select-all">https://intranet.hbtn.io/corrections/364239/correct</span><span class="input-group-btn"><a class="btn btn-default"><span data-container="body" data-html="false" data-placement="auto top" data-toggle="tooltip" title="" data-original-title="Click to copy"><span role="button"><i aria-hidden="true" class="fa fa-clipboard fa-fw"></i></span></span></a></span></div><p><span>Don't forget to <a href="/corrections/to_review">review one of them</a>.</span><strong> Reviews are due by <span data-container="body" data-html="false" data-placement="auto top" data-toggle="tooltip" title="" data-original-title="2022-07-30 00:00 (GMT-05:00)"><span class="datetime">Jul 30, 2022 12:00 AM</span></span></strong></p></div></div></div></div></div>


  </div>