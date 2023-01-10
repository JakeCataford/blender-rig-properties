Blender Rig Properties Addon
====

Addon for blender pose mode that allows easy access to custom properties that are defined on a bone named "PROPERTIES" in an armature. The custom properties of that bone will be shown in a "Rig Properties" panel at all times during pose mode.

Keying custom properties on a bone is the most consistent way I've found to export things like FK/IK switching, and blend shape animations to Unity because they end up encoded directly into the armatures action. Custom properties on the armature object don't get picked up in the same way. The downside of keying the custom properties on a bone is that the bone must be selected to access those properties. This plugin remedies that by allowing you to conventionally have a "PROPERTIES" bone and keeping all of the custom properties of that bone in a panel no matter which bones are selected. 

This feature was common in some animation tools such as the "space switcher" addon, but I wanted _only_ this feature for my rigs, so I adapted it here.