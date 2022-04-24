<h1>Stage 2/6: Correct syntax</h1>
<h5>Description</h5>
<p>You managed to fill in all the missing data and correct the mistakes with the types. However, you noticed that there are multiple problems with suffix names for the stops: sometimes they are incorrect, and sometimes they are simply missing. As if that was not enough, you also realized that there are errors in the arrival times.</p>
<p>It seems like you have to carefully look at the entire &quot;Format&quot; column in the first part of the documentation.</p>
<p>Here are the documents that you have:&nbsp;<a href="https://stepik.org/media/attachments/lesson/412967/Documentation.jpg" rel="noopener noreferrer nofollow" target="_blank">documentation<img src="http://localhost:63342/eduResources/icons/com/jetbrains/edu/learning/external_link_arrow@2x_dark.png" border="0" width="14" height="14"></a> and&nbsp;<a href="https://stepik.org/media/attachments/lesson/412967/Diagram_of_the_bus_line.jpg" rel="noopener noreferrer nofollow" target="_blank">diagram of the bus lines<img src="http://localhost:63342/eduResources/icons/com/jetbrains/edu/learning/external_link_arrow@2x_dark.png" border="0" width="14" height="14"></a>.</p>
<h5>Objectives</h5>
<ol>
    <li>The string containing the data in JSON format is passed to standard input.</li>
    <li>Check that the data format complies with the documentation.</li>
    <li>Only the fields that have such a requirement are relevant, i.e.&nbsp;stop_name,&nbsp;stop_type,&nbsp;a_time, so, please, count errors only for them.</li>
    <li>Like in the previous stage, print the information about the number of found errors in total and in each field. Remember that there might be no errors at all.</li>
    <li>The output should have the same formatting as shown in the example.</li>
</ol>
<p>If you can&apos;t find the necessary information in the stage description, it can probably be found in the attached documentation.</p>
<p>Note that the time format is military time (24 hours,&nbsp;hh:mm). That means that there are certain restrictions:</p>
<ul>
    <li>the first digit cannot be 3, 4, etc.;</li>
    <li>hours less than 10 should have zero in front of them, e.g.&nbsp;08:34;</li>
    <li>the delimiter should be colon&nbsp;:.</li>
</ul>
<h5>Example</h5>
<p>Input:</p>
<pre>[
    {
        &quot;bus_id&quot;: 128,
        &quot;stop_id&quot;: 1,
        &quot;stop_name&quot;: &quot;Prospekt Av.&quot;,
        &quot;next_stop&quot;: 3,
        &quot;stop_type&quot;: &quot;S&quot;,
        &quot;a_time&quot;: &quot;08:12&quot;
    },
    {
        &quot;bus_id&quot;: 128,
        &quot;stop_id&quot;: 3,
        &quot;stop_name&quot;: &quot;Elm Street&quot;,
        &quot;next_stop&quot;: 5,
        &quot;stop_type&quot;: &quot;&quot;,
        &quot;a_time&quot;: &quot;8:19&quot;
    },
    {
        &quot;bus_id&quot;: 128,
        &quot;stop_id&quot;: 5,
        &quot;stop_name&quot;: &quot;Fifth Avenue&quot;,
        &quot;next_stop&quot;: 7,
        &quot;stop_type&quot;: &quot;OO&quot;,
        &quot;a_time&quot;: &quot;08:25&quot;
    },
    {
        &quot;bus_id&quot;: 128,
        &quot;stop_id&quot;: 7,
        &quot;stop_name&quot;: &quot;Sesame Street&quot;,
        &quot;next_stop&quot;: 0,
        &quot;stop_type&quot;: &quot;F&quot;,
        &quot;a_time&quot;: &quot;08:77&quot;
    },
    {
        &quot;bus_id&quot;: 256,
        &quot;stop_id&quot;: 2,
        &quot;stop_name&quot;: &quot;Pilotow Street&quot;,
        &quot;next_stop&quot;: 3,
        &quot;stop_type&quot;: &quot;S&quot;,
        &quot;a_time&quot;: &quot;09:20&quot;
    },
    {
        &quot;bus_id&quot;: 256,
        &quot;stop_id&quot;: 3,
        &quot;stop_name&quot;: &quot;Elm&quot;,
        &quot;next_stop&quot;: 6,
        &quot;stop_type&quot;: &quot;&quot;,
        &quot;a_time&quot;: &quot;09:45&quot;
    },
    {
        &quot;bus_id&quot;: 256,
        &quot;stop_id&quot;: 6,
        &quot;stop_name&quot;: &quot;Sunset Boulevard&quot;,
        &quot;next_stop&quot;: 7,
        &quot;stop_type&quot;: &quot;A&quot;,
        &quot;a_time&quot;: &quot;09:59&quot;
    },
    {
        &quot;bus_id&quot;: 256,
        &quot;stop_id&quot;: 7,
        &quot;stop_name&quot;: &quot;Sesame Street&quot;,
        &quot;next_stop&quot;: 0,
        &quot;stop_type&quot;: &quot;F&quot;,
        &quot;a_time&quot;: &quot;10.12&quot;
    },
    {
        &quot;bus_id&quot;: 512,
        &quot;stop_id&quot;: 4,
        &quot;stop_name&quot;: &quot;bourbon street&quot;,
        &quot;next_stop&quot;: 6,
        &quot;stop_type&quot;: &quot;S&quot;,
        &quot;a_time&quot;: &quot;38:13&quot;
    },
    {
        &quot;bus_id&quot;: 512,
        &quot;stop_id&quot;: 6,
        &quot;stop_name&quot;: &quot;Sunset Boulevard&quot;,
        &quot;next_stop&quot;: 0,
        &quot;stop_type&quot;: &quot;F&quot;,
        &quot;a_time&quot;: &quot;08:16&quot;
    }
]</pre>
<p>Output:</p>
<pre>Format validation: 9 errors
stop_name: 3
stop_type: 2
a_time: 4</pre>
<p><br></p>