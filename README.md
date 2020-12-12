# yarn_cors_api #
About YARN API CORS description and demo.

## Background Note ##

A customer feedback they are undergoing CORS policy error, while they are trying to access YARN API.

Product is CDH 5.16.1, YARN version is 2.6.0.

Case number: 731997
Related cases: 722527

## What is CORS ##

For example:
While browsing "www.google.com", try to access "www.baidu.com", you would see below mesages:

![seeing CORS error][imageSeeingCorsError]

[imageSeeingCorsError]: ./docs/imgs/cosole_cors.png

The meesage is currently: "Access-Control-Allow-Origin header is present" , but it may vary in your case. Because there are several HTTP headers related to this CORS policy.

## A Demo to Reproduce CORS Access 

Please find the code in [here](./demo).
It's a simple web application build by Python Django.

Please do preparation below before you run:

1. Install Python 3
2. Install requirements via requirements.txt
3.  In "mysite/mysite/settings.py":
    
    1. `SECRET_KEY`
    2. `ALLOWED_HOSTS`

4.  In "mysite/yarn_cors_api_demo/views.py":

    1. `url = "http://kyan-cdh03.novalocal:8088/ws/v1/cluster/apps?deSelects=resourceRequests"` --> Your YARN RM URL

5.  In "mysite/yarn_cors_api_demo/static/js/api.js":
    
    1. `"http://kyan-cdh03.novalocal:8088/ws/v1/cluster/apps?deSelects=resourceRequests"` --> Your YARN RM URL

### A Video Showing the CORS blocking ###

[video demo - accessing YARN API blocked by CORS][imageVideoDemo]

[imageVideoDemo]: ./docs/imgs/cors_demo_compressed.mp4

## How to Enable CORS in YARN ##

### Note: 2.6.0 and 3.0.0 documentation is inconsistent ###

Note: I'm not sure in YARN [2.6.0][rMApi-2.6.0] if the CORS does work, because:
Comparing the documentation of 2.6.0 and [3.0.0][rMApi-3.0.0], there's no CORS related description in 2.6.0.

Below part is Only in 3.0.0:

> To enable cross-origin support (CORS) for the RM only(without enabling it for the NM), please set the following configuration parameters:
> 
> In core-site.xml, add org.apache.hadoop.security.HttpCrossOriginFilterInitializer to hadoop.http.filter.initializers. In yarn-site.xml, set yarn.resourcemanager.webapp.cross-origin.enabled to true.

[rMApi-2.6.0]: https://archive.cloudera.com/cdh5/cdh/5/hadoop-2.6.0-cdh5.12.0/hadoop-yarn/hadoop-yarn-site/ResourceManagerRest.html
[rMApi-3.0.0]: https://archive.cloudera.com/cdh6/6.0.1/docs/hadoop-3.0.0-cdh6.0.1/hadoop-yarn/hadoop-yarn-site/ResourceManagerRest.html#Enabling_CORS_support

### Instruction of Enabling CORS in YARN 3.0.0 ###

According to [3.0.0 documentation][rMApi-3.0.0] and CDP Private Cloud Base [documentation][cdpPrivCDoc].
Add these options on YARN service as below:

![YARN core-site.xml][corsRmCoreSite]
![YARN yarn-site.xml][corsYarnSite]

[cdpPrivCDoc]: https://docs.cloudera.com/cdp-private-cloud-base/7.1.3/yarn-security/topics/yarn-configure-cross-origin-support-for-yarn.html
[corsRmCoreSite]: ./docs/imgs/cors_core_site.png
[corsYarnSite]: ./docs/imgs/cors_yarn_site.png

### Notiice: Applying Above Settings Require Attention ###

When you applied above settings, the ResourceManager's UI would lost history records!
The data of records won't gone but due to some program logic, changing the `hadoop.http.filter.initializers` would result in this phenomenon!

So the best way to access YARN API is to use a proxy service, just like my code example 1!
You can use any proxy service, such as Nginx as reverse proxy, or write web application like the example code.

### A Video Showing CORS Working ###

[video demo - accessing YARN API blocked by CORS][YarnApiCorsEnabled]

[YarnApiCorsEnabled]: ./docs/imgs/yarn_cors_enabled_compressed.mp4
