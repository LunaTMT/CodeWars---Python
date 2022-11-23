import re

def check_length(string):

    

    if  len(string) >= 30:
        remove = ["the","of","in","from","by","with","and", "or", "for", "to", "at", "a"]
        list_of_words = string.lower().split("-")
        filtered_words = [word for word in list_of_words if word.lower() not in remove]
        final_string = ' '.join(filtered_words)

        return "".join([x[0].upper() for x in final_string.split(" ")])    
    return string.replace("-", " " )
        
 


def generate_bc(url, separator):
    url = url.split("/")

    if url[0] == "https:":
        url = url[2:]

    url_length = len(url)


    answer = [f"<a href=\"/\">HOME</a>",]
    breadcrumb = []

    for i in range(1, url_length):
        #print(url[i])


        if i == url_length - 1 or url[i] == 'docs':
            #last item 
            end = re.split('\.|\?', url[i])
            answer.append(f"<span class=\"active\">{check_length(end[0].upper())}</span>")   
            break
        
        breadcrumb.append(url[i])
        breadcrumb_trail = "/".join(breadcrumb)
        answer.append(f"<a href=\"/{breadcrumb_trail}/\">{check_length(url[i].upper())}</a>")

    print(f"{separator}".join(answer))
    return (f"{separator}".join(answer))


if __name__ == "__main__":
    #generate_bc("mysite.com/pictures/holidays.html", " : ")
    #'<a href="/">HOME</a> : <a href="/pictures/">PICTURES</a> : <span class="active">HOLIDAYS</span>'
    #&lt;a href="/"&gt;HOME&lt;/a&gt; : &lt;a href="/pictures/"&gt;PICTURES&lt;/a&gt; : &lt;span class="active"&gt;HOLIDAYS&lt;/span&gt; - instead got: &lt;a href="/"&gt;HOME&lt;/a&gt;  :  &lt;a href="/pictures/"&gt;PICTURES&lt;/a&gt;  :  &lt;span class="active"&gt;HOLIDAYS&lt;/span&gt;

    # '<a href="/">HOME</a> : 
    #  <a href="/pictures/">PICTURES</a> : 
    #  <span class="active">HOLIDAYS</span>')`

    #generate_bc("www.codewars.com/users/GiacomoSorbi?ref=CodeWars", " / ")
    # '<a href="/">HOME</a> / 
    #  <a href="/users/">USERS</a> / 
    #  <span class="active">GIACOMOSORBI</span>')
    
    #generate_bc("www.microsoft.com/important/confidential/docs/index.htm#top", " * ")
    # '<a href="/">HOME</a> * 
    #  <a href="/important/">IMPORTANT</a> * 
    #  <a href="/important/confidential/">CONFIDENTIAL</a> * 
    #  <span class="active">DOCS</span>')
    
    
    #generate_bc("mysite.com/very-long-url-to-make-a-silly-yet-meaningful-example/example.asp", " > ")
    # '<a href="/">HOME</a> > 
    #  <a href="/very-long-url-to-make-a-silly-yet-meaningful-example/">VLUMSYME</a> > 
    #  <span class="active">EXAMPLE</span>')
    
   
    #generate_bc("www.very-long-site_name-to-make-a-silly-yet-meaningful-example.com/users/giacomo-sorbi", " + ")
    #'<a href="/">HOME</a> + <a href="/users/">USERS</a> + <span class="active">GIACOMO SORBI</span>')
    # <a href="/">HOME</a> + <a href="/users/">USERS</a> + <span class="active">GIACOMO-SORBI</span>

    generate_bc("https://www.linkedin.com/in/giacomosorbi", " * ")
    #Exp
    #Got
    #&lt;a href="/"&gt;HOME&lt;/a&gt; * &lt;a href="/in/"&gt;IN&lt;/a&gt; * &lt;span class="active"&gt;GIACOMOSORBI&lt;/span&gt; 
    #&lt;a href="/"&gt;HOME&lt;/a&gt; * &lt;a href="/  /"&gt;  &lt;/a&gt; * &lt;a href="//www.linkedin.com/"&gt;WWW.LINKEDIN.COM&lt;/a&gt; * &lt;a href="//www.linkedin.com/in/"&gt;IN&lt;/a&gt; * &lt;span class="active"&gt;GIACOMOSORBI&lt;/span&gt;


#&lt;a href="/"&gt;HOME&lt;/a&gt; &gt; &lt;a href="/very-long-url-to-make-a-silly-yet-meaningful-example/"&gt;VLUMSYME&lt;/a&gt; &gt; &lt;span class="active"&gt;EXAMPLE&lt;/span&gt; 
#&lt;a href="/"&gt;HOME&lt;/a&gt; &gt; &lt;a href="/very-long-url-to-make-a-silly-yet-meaningful-example/"&gt;VLUTMASYME&lt;/a&gt; &gt; &lt;span class="active"&gt;EXAMPLE&lt;/span&gt;