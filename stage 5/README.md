<h1>Stage 5/6: Unlost in time</h1>
<h5>Description</h5>
<p>It is now time to move on to a more detailed analysis. First, check that arrival times for the upcoming stops make sense: they are supposed to be increasing, that is, going forward in time. After all, there is no information in the documentation that your company offers time travel.</p>
<p>Here are the documents that you have:&nbsp;<a href="https://stepik.org/media/attachments/lesson/412967/Documentation.jpg" rel="noopener noreferrer nofollow" target="_blank">documentation<img src="http://localhost:63342/eduResources/icons/com/jetbrains/edu/learning/external_link_arrow@2x_dark.png" border="0" width="14" height="14"></a> and&nbsp;<a href="https://stepik.org/media/attachments/lesson/412967/Diagram_of_the_bus_line.jpg" rel="noopener noreferrer nofollow" target="_blank">diagram of the bus lines<img src="http://localhost:63342/eduResources/icons/com/jetbrains/edu/learning/external_link_arrow@2x_dark.png" border="0" width="14" height="14"></a>.</p>
<h5>Objectives</h5>
<ol>
    <li>The string containing the data in JSON format is passed to standard input.</li>
    <li>Check that the arrival time for the upcoming stops for a given bus line is increasing.</li>
    <li>If the arrival time for the next stop is earlier than or equal to the time of the current stop, stop checking that bus line and remember the name of the incorrect stop.</li>
    <li>Display the information for those bus lines that have time anomalies. For the correct stops, do not display anything.</li>
    <li>If all the lines are correct timewise, print&nbsp;OK.</li>
    <li>The output should have the same formatting as shown in the example.</li>
</ol>
<p>If you can&apos;t find the necessary information in the stage description, it can probably be found in the attached documentation.</p>
<h5>Examples</h5>
<p><strong>Example 1</strong></p>
<p>Input 1:</p>
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
        &quot;a_time&quot;: &quot;08:17&quot;
    },
    {
        &quot;bus_id&quot;: 128,
        &quot;stop_id&quot;: 7,
        &quot;stop_name&quot;: &quot;Sesame Street&quot;,
        &quot;next_stop&quot;: 0,
        &quot;stop_type&quot;: &quot;F&quot;,
        &quot;a_time&quot;: &quot;08:07&quot;
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
        &quot;a_time&quot;: &quot;09:44&quot;
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
<p>Output 1:</p>
<pre>Arrival time test:
bus_id line 128: wrong time on station Fifth Avenue
bus_id line 256: wrong time on station Sunset Boulevard</pre>
<p><strong>Example 2</strong></p>
<p>Input 2:</p>
<pre>[
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
<p>Output 2:</p>
<pre>Arrival time test:
OK</pre>
<p><br></p>