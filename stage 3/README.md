<h1>Stage 3/6: Bus line info</h1>
<h5>Description</h5>
<p>It wasn&apos;t easy, but finally, you verified the data format and the required fields. It is now time to check how many bus lines we have and how many stops there are on each line. Before we can go further with sorting out the database, it would be a good idea to check that the information is complete.</p>
<p>Here are the documents that you have:&nbsp;<a href="https://stepik.org/media/attachments/lesson/412967/Documentation.jpg" rel="noopener noreferrer nofollow" target="_blank">documentation<img src="http://localhost:63342/eduResources/icons/com/jetbrains/edu/learning/external_link_arrow@2x_dark.png" border="0" width="14" height="14"></a> and&nbsp;<a href="https://stepik.org/media/attachments/lesson/412967/Diagram_of_the_bus_line.jpg" rel="noopener noreferrer nofollow" target="_blank">diagram of the bus lines<img src="http://localhost:63342/eduResources/icons/com/jetbrains/edu/learning/external_link_arrow@2x_dark.png" border="0" width="14" height="14"></a>.</p>
<h5>Objectives</h5>
<ol>
    <li>The string containing the data in JSON format is passed to standard input.</li>
    <li>Find the names of all the bus lines.</li>
    <li>Verify the number of stops for each line.</li>
    <li>The output should have the same formatting as shown in the example.</li>
</ol>
<p>If you can&apos;t find the necessary information in the stage description, it can probably be found in the attached documentation.</p>
<h5>Example</h5>
<p>Input:</p>
<pre>[
    {
        &quot;bus_id&quot;: 128,
        &quot;stop_id&quot;: 1,
        &quot;stop_name&quot;: &quot;Prospekt Avenue&quot;,
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
        &quot;a_time&quot;: &quot;08:19&quot;
    },
    {
        &quot;bus_id&quot;: 128,
        &quot;stop_id&quot;: 5,
        &quot;stop_name&quot;: &quot;Fifth Avenue&quot;,
        &quot;next_stop&quot;: 7,
        &quot;stop_type&quot;: &quot;O&quot;,
        &quot;a_time&quot;: &quot;08:25&quot;
    },
    {
        &quot;bus_id&quot;: 128,
        &quot;stop_id&quot;: 7,
        &quot;stop_name&quot;: &quot;Sesame Street&quot;,
        &quot;next_stop&quot;: 0,
        &quot;stop_type&quot;: &quot;F&quot;,
        &quot;a_time&quot;: &quot;08:37&quot;
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
        &quot;stop_name&quot;: &quot;Elm Street&quot;,
        &quot;next_stop&quot;: 6,
        &quot;stop_type&quot;: &quot;&quot;,
        &quot;a_time&quot;: &quot;09:45&quot;
    },
    {
        &quot;bus_id&quot;: 256,
        &quot;stop_id&quot;: 6,
        &quot;stop_name&quot;: &quot;Sunset Boulevard&quot;,
        &quot;next_stop&quot;: 7,
        &quot;stop_type&quot;: &quot;&quot;,
        &quot;a_time&quot;: &quot;09:59&quot;
    },
    {
        &quot;bus_id&quot;: 256,
        &quot;stop_id&quot;: 7,
        &quot;stop_name&quot;: &quot;Sesame Street&quot;,
        &quot;next_stop&quot;: 0,
        &quot;stop_type&quot;: &quot;F&quot;,
        &quot;a_time&quot;: &quot;10:12&quot;
    },
    {
        &quot;bus_id&quot;: 512,
        &quot;stop_id&quot;: 4,
        &quot;stop_name&quot;: &quot;Bourbon Street&quot;,
        &quot;next_stop&quot;: 6,
        &quot;stop_type&quot;: &quot;S&quot;,
        &quot;a_time&quot;: &quot;08:13&quot;
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
<pre>Line names and number of stops:
bus_id: 128, stops: 4
bus_id: 256, stops: 4
bus_id: 512, stops: 2</pre>
<p><br></p>