# Project 4 - Full Stack Django App

## Overview

We are going to make a Full Stack App.  This means a frontend _and_ a backend.  Your backend will be written in Django.

## Project Proposals

You will be meeting with your Squad leader on Monday to get your project idea approved

### Due Sunday, June 17 at 11:00PM

A new Github Repo that includes the following sections

* Introduction
  - A game blog that introduces console games with CRUD for user's to keep a list of games to display and vote
* Technologies
  - javascript(jquery) django, postgres, external API
* MVP
  - user auth login/logout
  - user can CRUD their list of games
  - AJAX from external IGDB with a key to pull console game information
* Goals
  - pulling in game plays
* Stretch Goals
  - get external content such as game play instead of cinematic trailers.
* Timeline
  - Monday night - create user auth, have CRUD on creating a game post
  - Tuesday night - complete test cases and deploy to Heroku
  - Wednesday night - styling and external API
  - Thursday night - 
* Wireframes
  - You can use whatever you want to make these (it can just be a drawing)
  - This must be checked into your repo and displayed in this section
  - If it's a drawing you can take a picture with your phone and upload it :)
* Crow's foot diagram of your schema.


## Technical Requirements

Everything is in the same repo you created for your proposal

### Due Thursday, June 21 at 11:00PM

Your project must:

* Be **Full CRUD**: `Create && Read && Update && Destroy`
* Have **authentication**.  Users can log in and out.  A user should not have the ability to see or update any data that you don't want them to
* **Tests**. You need to have at least a few tests per app.  All tests must pass.
* **Postgres database** with **multiple related database tables**.
* Do _something_ on the frontend (does not have to be as much as Project 1)
  - You are still using Django to serve up the pages
  - But the pages are not completely static - the user can interact with it
* Use **Vanilla Javascript or jQuery** for **DOM manipulation**
  - Do not have a heavy mix of both
  - If you are using Vanilla JS: we should see no `$` (unless it's used for AJAX)
  - If you are using jQuery: we should see no `document`
* Use at least one of the following (and your README should tell us what option(s) used)
  - **Ajax requests to your Django app**.  This means you have route that responds with JSON and your frontend makes an AJAX request to it.
  - [**`requests`**](http://docs.python-requests.org/en/master/). Make an HTTP from the backend to some API.
  - **Typescript**.  Use Typescript on your frontend instead of of Javascript.
  - **Full test coverage**.  At least one test per route per verb.  If the route does something different depending on whether or not someone is logged in. Test both cases.  All tests must pass.
  - **Something else** that will **blow us away**.  Talk to your squad leader if you can't make any of the above work.
* Be **deployed on Heroku**
  - Your app must work on Heroku, not just locally
* Have all your code on our **GitHub Enterprise**
  - We cannot see your code on Heroku, we can only see it on GitHub (the same repo where your proposal is)
  - This means you have two remotes, `heroku` and `origin`
* Use **CSS**.  You may use Bootstrap but you also need to have some of your own CSS.
* Have at least 40 commits. (You will likely have many more)
* Have code that we can read.  If the indentation is all over place, variable / function names that don't make sense, etc. then we cannot read your code.  We have to read your code in order to grade it.
* A `README.md` (see below)
* **Absolutely no Disney IP**.  If you have any doubts, do not use it
  - This is a reminder.  This goes for every assignment

### `README`

Your `README` (by Thursday night) should include

* (Every section from the proposal)
* Struggles
  - What were the challenging parts?  Tell us about it.  What did you learn?
* App
  - A link to the deployed app
  - Screen shots of the different pages of the app
  - Any other info we should know
* Future Goals
  - Tell us what would like to add/fix/remove/change with more time


## Suggested Ways to Get Unstuck

* **Break the project down into different components** (data, presentation, views, style, DOM manipulation) and brainstorm each component individually. Use whiteboards!
* **Use your Development Tools** (`console.log`, `debugger`, inspector, `alert` statements, etc) to debug and solve problems
* Work through the lessons in class & ask questions when you need to! Think about adding relevant code to your app each night, instead of, you know... _procrastinating_.
* **Commit early, commit often.** Don’t be afraid to break something because you can always go back in time to a previous version.
* Consult **documentation resources** (MDN, jQuery, etc.) at home to better understand what you’ll be getting into.
* Consult **previous lectures**
* **Don’t be afraid to write code that you know you will have to remove later.** Create temporary elements (buttons, links, etc) that trigger events if real data is not available.
* Read the error message.  Google the error message.


## Friendly reminder

Do not accidentally plagiarize. [Cite your sources](https://git.generalassemb.ly/code-rosie/student_resources/blob/master/plagiarism.md#how-to-get-around-plagiarism)

## Project Feedback + Evaluation

Refer to our [Project Rubric](https://git.generalassemb.ly/code-rosie/student_resources/blob/master/project-rubric.md)

## Asking for you help

Refer to [these instructions](https://git.generalassemb.ly/code-rosie/student_resources/blob/master/project-week-help.md)



## What happens during project week

* Like any other day, you must be here from 9 to 5
* You will meet with your squad for standup daily
* You are in charge of your own time management
  - We will help as needed but getting the job done is **your responsibility**
* You will present your project on Friday (more on this as the date gets closer)
