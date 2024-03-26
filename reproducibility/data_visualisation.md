<p align="center">
 <picture>
 <img src="https://github.com/jackv-murray/lastfm-scrobble-analysis/blob/main/assets/section%206.png" width="800">
 </picture>
 </p>

 ## Tableau Public
 To build the dashboard you'll require a data visualisation tool. Google Cloud comes with a free version of [Looker Studio](https://lookerstudio.google.com/overview), however there are more powerful and better-supported tools available, such as Tableau. 

 Tableau Public is a completely free version of the licensed Tableau Desktop tool, all hosted online which allows you to share your visualisations and build a portfolio of dashboards. 

You can create a new account  [here](https://public.tableau.com/en-gb/s/#modal-signup) and [explore](https://public.tableau.com/app/discover) some of the community-created dashboards for inspiration. 

### Getting started with Tableau
Tableau has a great learning community and the tool has been available for a long time with plenty of updates over the years introducing new features and optimisations, meaning there's plenty of resources available.

I would recommend the following if you want to learn how to use Tableau:
1. [Tableau - Get Started](https://www.tableau.com/en-gb/learn/get-started)
2. [eLearning at Tableau](https://www.tableau.com/en-gb/learn/training/elearning)   *paid but worth it if there's a training budget*
3. [Flerlage Twins](https://www.flerlagetwins.com/)
4. [Tableau Tim](https://www.youtube.com/@TableauTim)

## The 'Scrobble Analysis' Dashboard
Here I'll talk about the design and development process. I won't go into the details on **how** to create the specific visualisations. Instead, I'll focus on more the more broader steps taken to create the dashboard.

### Wireframe design
Before creating anything in Tableau, it's usually a good idea to first create a wireframe, or template design. There are many tools available to aid you with this, such as [Figma](https://www.figma.com/). The Idea is to create
a rough design of your dashboard, usually with stakeholder input, to plan out what metrics should be included and how that might look.

### Design best practices

[Whitespace](https://playfairdata.com/dashboard-element-5-white-space/) - The use of whitespace in dashboards creates a separation between the different charts and helps the viewer process the information in front of them. 
Plus, it's much neater having distinct, separated spaces for each of your charts.

[Eliminating noise](https://www.thedataschool.co.uk/tobias-fitschen/dashboard-design-best-practices/) - By default, Tableau graphs will contain gridlines, axis headers, labels etc. You can remove or tone these down so your viewer can focus on the important aspects of your dashboard.

[Use of colour](https://www.thedataschool.co.uk/tobias-fitschen/dashboard-design-best-practices-color/) - Consider matching colours to your company's logos or colours scheme to create a distinct, associated theme. You can also add accessibility by using colour-blind friendly palletes.

[Chart selection](https://public.tableau.com/app/profile/adedamola8122/viz/ChartSelectionGuide2/Dashboard) - What kind of graph is suitable for the type of data you have, and the story you want to tell with it? Avoid unhelpful graph types such as pie charts and keep it simple and purposeful.
