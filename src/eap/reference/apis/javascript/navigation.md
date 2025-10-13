---
tags: navigation, mobile apps, reactive web apps, back handlers, transition animations
summary: OutSystems Developer Cloud (ODC) enhances navigation in mobile and reactive web apps with custom back handlers and transition animations.
locale: en-us
guid: 2726ff0c-6682-45e1-88eb-067d0cc6f57d
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
coverage-type:
  - remember
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
  - odc portal
---
# Navigation

Provides the ability to perform normal and history navigations, and to override some navigation behaviors (e.g. back). Used to create new transition animations instead of overriding the existing ones using CSS.

The functions below related with BackHandlers ([registerBackNavigationHandler](#registerbacknavigationhandler) and [unregisterBackNavigationHandler](#unregisterbacknavigationhandler)) are used to manipulate the behavior of back actions, e.g. pressing the Back button in Android. A common use case is when the Back button is pressed just to close a menu instead of navigating to the previous screen.

## Summary

|Functions|Description|
|---|---|
|[navigateBack](#navigateback)|Performs a back navigation, using an optional transition animation.|
|[navigateForward](#navigateforward)|Performs a forward navigation, using an optional transition animation.|
|[navigateTo](#navigateto)|Performs a navigation to a provided URL using an optional transition animation.|
|[navigatedFromHistory](#navigatedfromhistory)|Checks if the current screen was loaded from the browser's history.|
|[registerBackNavigationHandler](#registerbacknavigationhandler)|Registers a callback function in a queue to be called when navigating back.|
|[registerNavigationHandler](#registernavigationhandler)| Overrides the navigation handler with a provided callback.|

## Functions

### navigateBack

**navigateBack([transition: TransitionAnimation \| string]): void**

Performs a back navigation, using an optional transition animation.

If there are registered back event handlers, the last registered one is executed. Otherwise, a navigation to the previous screen is performed. If the current screen is the first one opened on a mobile application, the application is closed.

Example:

```javascript
// navigate to the previous screen using a 'Slide from Left' transition animation
$public.Navigation.navigateBack(3);
```

Parameters:

* (Optional) **transition**: TransitionAnimation \| string<br/>Either a known transition type or a string representing the prefix of the CSS classes used to animate the transition.<br/>If a value is not provided, the animation used to enter the current screen is reversed and used.
<br/><br/>The TransitionAnimation parameter is represented by a number that correspond to the animation type to use:
    * 0 = None. No animation will be shown when navigating to the previous screen.
    * 1 = Default. The default animation will be shown when navigating to the previous screen. The default animation is for the previous screen to slide in from the right of the screen, moving right-to-left.  
    * 2 = Fade. A fade-in animation will be shown when navigating to the previous screen.
    * 3 = Slide from Left. The previous screen will slide in from the left of the screen, moving from left-to-right.
    * 4 = Slide from Right. The previous screen will slide in from the right of the screen, moving from right-to-left.
    * 5 = Slide from Bottom. The previous screen will slide in from the bottom of the screen, moving from bottom-to-top.
    * 6 = Slide from Top. The previous screen will slide in from the top of the screen, moving from top-to-bottom.

Returns: void

### navigateForward

**navigateForward([transition: TransitionAnimation \| string]): void**

Performs a forward navigation, using an optional transition animation.

The forward navigation is performed if the current screen was entered using a back navigation; otherwise, no navigation is performed.

Example:

```javascript
// perform a forward navigation using a 'Slide from Right' transition animation
$public.Navigation.navigateForward(4);
```

Parameters:

* (Optional) **transition**: TransitionAnimation \| string<br/>Either a known transition type or a string representing the prefix of the CSS classes used to animate the transition.<br/>If a value is not provided, the animation used to enter the current screen is used.
  <br/><br/>The `TransitionAnimation` parameter is represented by a number that correspond to the animation type to use:
    * 0 = None. No animation will be shown when navigating to the next screen.
    * 1 = Default. The default animation will be shown when navigating to the next screen. The default animation is for the next screen to slide in from the right of the screen, moving right-to-left.
    * 2 = Fade. A fade-in animation will be shown when navigating to the next screen.
    * 3 = Slide from Left. The next screen will slide in from the left of the screen, moving from left-to-right.
    * 4 = Slide from Right. The next screen will slide in from the right of the screen, moving from right-to-left.
    * 5 = Slide from Bottom. The next screen will slide in from the bottom of the screen, moving from bottom-to-top.
    * 6 = Slide from Top. The next screen will slide in from the top of the screen, moving from top-to-bottom.

Returns: void

### navigateTo

**navigateTo(url: string, [transition: TransitionAnimation \| string], [replace: boolean]): void**

Performs a navigation to a provided URL using an optional transition animation.

Parameters:

* **url**: string<br/>Relative or absolute URL to navigate to. If the URL points to a screen of the application, the transition will be animated according to the value of the `transition` parameter. Otherwise, a normal browser navigation is done.
* (Optional) **transition**: TransitionAnimation \| string<br/>Either a known transition type or a string representing the prefix of the CSS classes used to animate the transition.<br/>If a value is not provided, the animation used to enter the current screen is used.<br/>If a transition to an external site occurs, no animation will be used, regardless of the value provided for this parameter.
  <br/><br/>The TransitionAnimation parameter is represented by a number that correspond to the animation type to use:
    * 0 = None. No animation will be shown when navigating to the next screen.
    * 1 = Default. The default animation will be shown when navigating to the next screen. The default animation is for the next screen to slide in from the right of the screen, moving right-to-left.
    * 2 = Fade. A fade-in animation will be shown when navigating to the next screen.
    * 3 = Slide from Left. The next screen will slide in from the left of the screen, moving from left-to-right.
    * 4 = Slide from Right. The next screen will slide in from the right of the screen, moving from right-to-left.
    * 5 = Slide from Bottom. The next screen will slide in from the bottom of the screen, moving from bottom-to-top.
    * 6 = Slide from Top. The next screen will slide in from the top of the screen, moving from top-to-bottom.
* (Optional) **replace**: boolean<br/>Indicates if the navigation should replace the current history entry, instead of creating a new one that the user can navigate back to. If a value is not provided, the default is `false`.

Returns: void

### navigatedFromHistory

**navigatedFromHistory(): boolean**

Checks if the current screen was loaded from the browser's history.

Returns: boolean

Returns `true` if the current screen was loaded from the browser's history, `false` otherwise.

### registerBackNavigationHandler

**registerBackNavigationHandler(handlerCallback: function): number**

Registers a callback function in a queue to be called when navigating back.

When the 'back' event is triggered, the last inserted handler is called and removed from the queue. If no event handler is registered, it performs a navigation to the previous screen, reversing the transition animation used to reach the current screen, if one was used.

Example:

```javascript
// prevent the user from navigating back when a custom sidebar menu is being displayed

var menuBackHandler = function() {
  hideSidebarMenu();
};

showSidebarMenu();
$public.Navigation.registerBackNavigationHandler(menuBackHandler);

// this back navigation will just hide the menu
$public.Navigation.navigateBack();
```

Parameters:

* **handlerCallback**: function<br/>Callback to be called when a back event occurs.

Returns: number

ID of the registered callback.

### unregisterBackNavigationHandler

**unregisterBackNavigationHandler(id: number): void**

Unregisters a previously registered callback.

If no callback exists with the provided id, no action is taken.

Parameters:

* **id**: number<br/>ID of the callback to be unregistered.

Returns: void

### registerNavigationHandler

**handlerCallback: NavigationHandler**

Registers a synchronous callback, `handlerCallback`, to be called when a navigation event occurs. If the callback returns a true, the navigation will proceed normally, if false, the navigation is cancelled.

Parameters:

* **handlerCallback**: function<br/>Callback to be called when a navigation event occurs

Returns: void

## Type aliases

### NavigationHandler

**(url: string, [transition: TransitionAnimation \| string], [replace: boolean]) => void**

Parameters:

* **nextUrl**: string<br/>A string representation of the URL to navigate to as a part of the navigation event.
* **navigate**: [NavigationMethod](#navigationmethod)<br/>A function that can issue a new navigation from within the context of the previous navigation.

Returns: boolean. If `true`, the navigation occurs. Otherwise, the navigation is cancelled.

### NavigationMethod

Parameters:

* **url**: string<br/>The new URL to navigate to
* (Optional) **transition**: TransitionAnimation \| string<br/>Either a known transition type or a string representing the prefix of the CSS classes used to animate the transition.<br/>If a value is not provided, the animation used to enter the current screen is reversed and used.
  <br/><br/>The TransitionAnimation parameter is represented by a number that correspond to the animation type to use:
    * 0 = None. No animation will be shown when navigating to the previous screen.
    * 1 = Default. The default animation will be shown when navigating to the previous screen. The default animation is for the previous screen to slide in from the right of the screen, moving right-to-left.
    * 2 = Fade. A fade-in animation will be shown when navigating to the previous screen.
    * 3 = Slide from Left. The previous screen will slide in from the left of the screen, moving from left-to-right.
    * 4 = Slide from Right. The previous screen will slide in from the right of the screen, moving from right-to-left.
    * 5 = Slide from Bottom. The previous screen will slide in from the bottom of the screen, moving from bottom-to-top.
    * 6 = Slide from Top. The previous screen will slide in from the top of the screen, moving from top-to-bottom.
* (Optional) **replace**: boolean<br/>Indicates if the navigation should replace the current history entry, instead of creating a new one that the user can navigate back to. If a value is not provided, the default is `false`.

Returns: void
