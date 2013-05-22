#!/usr/bin/python
import gtk, os, gobject
import subprocess
from twisted.internet import gtk2reactor
gtk2reactor.install()
from twisted.internet import reactor
from threading import Thread
from twisted.internet.protocol import ProcessProtocol
gtk.gdk.threads_init()
global gui
gui='''<?xml version="1.0"?>
<interface>
  <requires lib="gtk+" version="2.16"/>
  <!-- interface-naming-policy project-wide -->
  <object class="GtkWindow" id="win-main">
    <property name="title" translatable="yes">ACube GUI</property>
    <property name="window_position">center</property>
    <signal name="remove" handler="on_window1_remove"/>
    <child>
      <object class="GtkVBox" id="vbox1">
        <property name="visible">True</property>
        <property name="orientation">vertical</property>
        <child>
          <object class="GtkMenuBar" id="menubar1">
            <property name="visible">True</property>
            <child>
              <object class="GtkMenuItem" id="menuitem1">
                <property name="visible">True</property>
                <property name="label" translatable="yes">_File</property>
                <property name="use_underline">True</property>
                <child type="submenu">
                  <object class="GtkMenu" id="menu1">
                    <property name="visible">True</property>
                    <child>
                      <object class="GtkImageMenuItem" id="imagemenuitem1">
                        <property name="label">gtk-new</property>
                        <property name="visible">True</property>
                        <property name="use_underline">True</property>
                        <property name="use_stock">True</property>
                      </object>
                    </child>
                    <child>
                      <object class="GtkImageMenuItem" id="imagemenuitem2">
                        <property name="label">gtk-open</property>
                        <property name="visible">True</property>
                        <property name="use_underline">True</property>
                        <property name="use_stock">True</property>
                      </object>
                    </child>
                    <child>
                      <object class="GtkImageMenuItem" id="imagemenuitem3">
                        <property name="label">gtk-save</property>
                        <property name="visible">True</property>
                        <property name="use_underline">True</property>
                        <property name="use_stock">True</property>
                      </object>
                    </child>
                    <child>
                      <object class="GtkImageMenuItem" id="imagemenuitem4">
                        <property name="label">gtk-save-as</property>
                        <property name="visible">True</property>
                        <property name="use_underline">True</property>
                        <property name="use_stock">True</property>
                      </object>
                    </child>
                    <child>
                      <object class="GtkSeparatorMenuItem" id="separatormenuitem1">
                        <property name="visible">True</property>
                      </object>
                    </child>
                    <child>
                      <object class="GtkImageMenuItem" id="imagemenuitem5">
                        <property name="label">gtk-quit</property>
                        <property name="visible">True</property>
                        <property name="use_underline">True</property>
                        <property name="use_stock">True</property>
                        <signal name="activate" handler="gtk_main_quit"/>
                      </object>
                    </child>
                  </object>
                </child>
              </object>
            </child>
            <child>
              <object class="GtkMenuItem" id="menuitem2">
                <property name="visible">True</property>
                <property name="label" translatable="yes">_Edit</property>
                <property name="use_underline">True</property>
                <child type="submenu">
                  <object class="GtkMenu" id="menu2">
                    <property name="visible">True</property>
                    <child>
                      <object class="GtkImageMenuItem" id="imagemenuitem6">
                        <property name="label">gtk-cut</property>
                        <property name="visible">True</property>
                        <property name="use_underline">True</property>
                        <property name="use_stock">True</property>
                      </object>
                    </child>
                    <child>
                      <object class="GtkImageMenuItem" id="imagemenuitem7">
                        <property name="label">gtk-copy</property>
                        <property name="visible">True</property>
                        <property name="use_underline">True</property>
                        <property name="use_stock">True</property>
                      </object>
                    </child>
                    <child>
                      <object class="GtkImageMenuItem" id="imagemenuitem8">
                        <property name="label">gtk-paste</property>
                        <property name="visible">True</property>
                        <property name="use_underline">True</property>
                        <property name="use_stock">True</property>
                      </object>
                    </child>
                    <child>
                      <object class="GtkImageMenuItem" id="imagemenuitem9">
                        <property name="label">gtk-delete</property>
                        <property name="visible">True</property>
                        <property name="use_underline">True</property>
                        <property name="use_stock">True</property>
                      </object>
                    </child>
                  </object>
                </child>
              </object>
            </child>
            <child>
              <object class="GtkMenuItem" id="menuitem3">
                <property name="visible">True</property>
                <property name="label" translatable="yes">_View</property>
                <property name="use_underline">True</property>
              </object>
            </child>
            <child>
              <object class="GtkMenuItem" id="menuitem4">
                <property name="visible">True</property>
                <property name="label" translatable="yes">_Help</property>
                <property name="use_underline">True</property>
                <child type="submenu">
                  <object class="GtkMenu" id="menu3">
                    <property name="visible">True</property>
                    <child>
                      <object class="GtkImageMenuItem" id="imagemenuitem10">
                        <property name="label">gtk-about</property>
                        <property name="visible">True</property>
                        <property name="use_underline">True</property>
                        <property name="use_stock">True</property>
                      </object>
                    </child>
                  </object>
                </child>
              </object>
            </child>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="position">0</property>
          </packing>
        </child>
        <child>
          <object class="GtkTable" id="table1">
            <property name="visible">True</property>
            <property name="border_width">1</property>
            <property name="n_rows">3</property>
            <property name="n_columns">4</property>
            <child>
              <object class="GtkTable" id="table2">
                <property name="visible">True</property>
                <property name="n_rows">3</property>
                <property name="n_columns">3</property>
                <child>
                  <object class="GtkButton" id="btn-LBU">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                    <property name="image">img-LBU</property>
                    <property name="relief">none</property>
                    <property name="focus_on_click">False</property>
                    <property name="image_position">right</property>
                    <signal name="clicked" handler="cubie_pressed"/>
                  </object>
                </child>
                <child>
                  <object class="GtkButton" id="btn-LU">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                    <property name="image">img-LU</property>
                    <property name="relief">none</property>
                    <property name="focus_on_click">False</property>
                    <signal name="clicked" handler="cubie_pressed"/>
                  </object>
                  <packing>
                    <property name="left_attach">1</property>
                    <property name="right_attach">2</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkButton" id="btn-LUF">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                    <property name="image">img-LUF</property>
                    <property name="relief">none</property>
                    <property name="focus_on_click">False</property>
                    <signal name="clicked" handler="cubie_pressed"/>
                  </object>
                  <packing>
                    <property name="left_attach">2</property>
                    <property name="right_attach">3</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkButton" id="btn-LB">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                    <property name="image">img-LB</property>
                    <property name="relief">none</property>
                    <property name="focus_on_click">False</property>
                    <signal name="clicked" handler="cubie_pressed"/>
                  </object>
                  <packing>
                    <property name="top_attach">1</property>
                    <property name="bottom_attach">2</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkButton" id="btn-L">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                    <property name="image">img-L</property>
                    <property name="relief">none</property>
                    <property name="focus_on_click">False</property>
                  </object>
                  <packing>
                    <property name="left_attach">1</property>
                    <property name="right_attach">2</property>
                    <property name="top_attach">1</property>
                    <property name="bottom_attach">2</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkButton" id="btn-LF">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                    <property name="image">img-LF</property>
                    <property name="relief">none</property>
                    <property name="focus_on_click">False</property>
                    <signal name="clicked" handler="cubie_pressed"/>
                  </object>
                  <packing>
                    <property name="left_attach">2</property>
                    <property name="right_attach">3</property>
                    <property name="top_attach">1</property>
                    <property name="bottom_attach">2</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkButton" id="btn-LDB">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                    <property name="image">img-LDB</property>
                    <property name="relief">none</property>
                    <property name="focus_on_click">False</property>
                    <signal name="clicked" handler="cubie_pressed"/>
                  </object>
                  <packing>
                    <property name="top_attach">2</property>
                    <property name="bottom_attach">3</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkButton" id="btn-LD">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                    <property name="image">img-LD</property>
                    <property name="relief">none</property>
                    <signal name="clicked" handler="cubie_pressed"/>
                  </object>
                  <packing>
                    <property name="left_attach">1</property>
                    <property name="right_attach">2</property>
                    <property name="top_attach">2</property>
                    <property name="bottom_attach">3</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkButton" id="btn-LFD">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                    <property name="image">img-LFD</property>
                    <property name="relief">none</property>
                    <property name="focus_on_click">False</property>
                    <property name="yalign">0.4699999988079071</property>
                    <signal name="clicked" handler="cubie_pressed"/>
                  </object>
                  <packing>
                    <property name="left_attach">2</property>
                    <property name="right_attach">3</property>
                    <property name="top_attach">2</property>
                    <property name="bottom_attach">3</property>
                  </packing>
                </child>
              </object>
              <packing>
                <property name="top_attach">1</property>
                <property name="bottom_attach">2</property>
              </packing>
            </child>
            <child>
              <object class="GtkTable" id="table3">
                <property name="visible">True</property>
                <property name="n_rows">3</property>
                <property name="n_columns">3</property>
                <property name="homogeneous">True</property>
                <child>
                  <object class="GtkButton" id="btn-FU">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                    <property name="image">img-FU</property>
                    <property name="relief">none</property>
                    <property name="focus_on_click">False</property>
                    <signal name="clicked" handler="cubie_pressed"/>
                  </object>
                  <packing>
                    <property name="left_attach">1</property>
                    <property name="right_attach">2</property>
                    <property name="x_options"></property>
                    <property name="y_options"></property>
                  </packing>
                </child>
                <child>
                  <object class="GtkButton" id="btn-FUR">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                    <property name="image">img-FUR</property>
                    <property name="relief">none</property>
                    <property name="focus_on_click">False</property>
                    <signal name="clicked" handler="cubie_pressed"/>
                  </object>
                  <packing>
                    <property name="left_attach">2</property>
                    <property name="right_attach">3</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkButton" id="btn-FL">
                    <property name="visible">True</property>
                    <property name="can_focus">False</property>
                    <property name="receives_default">True</property>
                    <property name="extension_events">cursor</property>
                    <property name="image">img-FL</property>
                    <property name="relief">none</property>
                    <property name="focus_on_click">False</property>
                    <signal name="clicked" handler="cubie_pressed"/>
                  </object>
                  <packing>
                    <property name="top_attach">1</property>
                    <property name="bottom_attach">2</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkButton" id="btn-F">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                    <property name="image">img-F</property>
                    <property name="relief">none</property>
                    <property name="focus_on_click">False</property>
                  </object>
                  <packing>
                    <property name="left_attach">1</property>
                    <property name="right_attach">2</property>
                    <property name="top_attach">1</property>
                    <property name="bottom_attach">2</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkButton" id="btn-FR">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                    <property name="image">img-FR</property>
                    <property name="relief">none</property>
                    <property name="focus_on_click">False</property>
                    <signal name="clicked" handler="cubie_pressed"/>
                  </object>
                  <packing>
                    <property name="left_attach">2</property>
                    <property name="right_attach">3</property>
                    <property name="top_attach">1</property>
                    <property name="bottom_attach">2</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkButton" id="btn-FDL">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                    <property name="image">img-FDL</property>
                    <property name="relief">none</property>
                    <property name="focus_on_click">False</property>
                    <signal name="clicked" handler="cubie_pressed"/>
                  </object>
                  <packing>
                    <property name="top_attach">2</property>
                    <property name="bottom_attach">3</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkButton" id="btn-FD">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                    <property name="image">img-FD</property>
                    <property name="relief">none</property>
                    <property name="focus_on_click">False</property>
                    <signal name="clicked" handler="cubie_pressed"/>
                  </object>
                  <packing>
                    <property name="left_attach">1</property>
                    <property name="right_attach">2</property>
                    <property name="top_attach">2</property>
                    <property name="bottom_attach">3</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkButton" id="btn-FRD">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                    <property name="image">img-FRD</property>
                    <property name="relief">none</property>
                    <property name="focus_on_click">False</property>
                    <signal name="clicked" handler="cubie_pressed"/>
                  </object>
                  <packing>
                    <property name="left_attach">2</property>
                    <property name="right_attach">3</property>
                    <property name="top_attach">2</property>
                    <property name="bottom_attach">3</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkButton" id="btn-FLU">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                    <property name="image">img-FLU</property>
                    <property name="relief">none</property>
                    <property name="focus_on_click">False</property>
                    <signal name="clicked" handler="cubie_pressed"/>
                  </object>
                </child>
              </object>
              <packing>
                <property name="left_attach">1</property>
                <property name="right_attach">2</property>
                <property name="top_attach">1</property>
                <property name="bottom_attach">2</property>
              </packing>
            </child>
            <child>
              <object class="GtkTable" id="table4">
                <property name="visible">True</property>
                <property name="n_rows">3</property>
                <property name="n_columns">3</property>
                <child>
                  <object class="GtkButton" id="btn-RFU">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                    <property name="image">img-RFU</property>
                    <property name="relief">none</property>
                    <property name="focus_on_click">False</property>
                    <signal name="clicked" handler="cubie_pressed"/>
                  </object>
                </child>
                <child>
                  <object class="GtkButton" id="btn-RF">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                    <property name="image">img-RF</property>
                    <property name="relief">none</property>
                    <property name="focus_on_click">False</property>
                    <signal name="clicked" handler="cubie_pressed"/>
                  </object>
                  <packing>
                    <property name="top_attach">1</property>
                    <property name="bottom_attach">2</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkButton" id="btn-RDF">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                    <property name="image">img-RDF</property>
                    <property name="relief">none</property>
                    <property name="focus_on_click">False</property>
                    <signal name="clicked" handler="cubie_pressed"/>
                  </object>
                  <packing>
                    <property name="top_attach">2</property>
                    <property name="bottom_attach">3</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkButton" id="btn-RU">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                    <property name="image">img-RU</property>
                    <property name="relief">none</property>
                    <property name="focus_on_click">False</property>
                    <signal name="clicked" handler="cubie_pressed"/>
                  </object>
                  <packing>
                    <property name="left_attach">1</property>
                    <property name="right_attach">2</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkButton" id="btn-R">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                    <property name="image">img-R</property>
                    <property name="relief">none</property>
                    <property name="focus_on_click">False</property>
                  </object>
                  <packing>
                    <property name="left_attach">1</property>
                    <property name="right_attach">2</property>
                    <property name="top_attach">1</property>
                    <property name="bottom_attach">2</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkButton" id="btn-RD">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                    <property name="image">img-RD</property>
                    <property name="relief">none</property>
                    <property name="focus_on_click">False</property>
                    <signal name="clicked" handler="cubie_pressed"/>
                  </object>
                  <packing>
                    <property name="left_attach">1</property>
                    <property name="right_attach">2</property>
                    <property name="top_attach">2</property>
                    <property name="bottom_attach">3</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkButton" id="btn-RUB">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                    <property name="image">img-RUB</property>
                    <property name="relief">none</property>
                    <property name="focus_on_click">False</property>
                    <signal name="clicked" handler="cubie_pressed"/>
                  </object>
                  <packing>
                    <property name="left_attach">2</property>
                    <property name="right_attach">3</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkButton" id="btn-RB">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                    <property name="image">img-RB</property>
                    <property name="relief">none</property>
                    <property name="focus_on_click">False</property>
                    <signal name="clicked" handler="cubie_pressed"/>
                  </object>
                  <packing>
                    <property name="left_attach">2</property>
                    <property name="right_attach">3</property>
                    <property name="top_attach">1</property>
                    <property name="bottom_attach">2</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkButton" id="btn-RBD">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                    <property name="image">img-RBD</property>
                    <property name="relief">none</property>
                    <property name="focus_on_click">False</property>
                    <signal name="clicked" handler="cubie_pressed"/>
                  </object>
                  <packing>
                    <property name="left_attach">2</property>
                    <property name="right_attach">3</property>
                    <property name="top_attach">2</property>
                    <property name="bottom_attach">3</property>
                  </packing>
                </child>
              </object>
              <packing>
                <property name="left_attach">2</property>
                <property name="right_attach">3</property>
                <property name="top_attach">1</property>
                <property name="bottom_attach">2</property>
              </packing>
            </child>
            <child>
              <object class="GtkTable" id="table5">
                <property name="visible">True</property>
                <property name="n_rows">3</property>
                <property name="n_columns">3</property>
                <child>
                  <object class="GtkButton" id="btn-BRU">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                    <property name="image">img-BRU</property>
                    <property name="relief">none</property>
                    <property name="focus_on_click">False</property>
                    <signal name="clicked" handler="cubie_pressed"/>
                  </object>
                </child>
                <child>
                  <object class="GtkButton" id="btn-BU">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                    <property name="image">img-BU</property>
                    <property name="relief">none</property>
                    <property name="focus_on_click">False</property>
                    <signal name="clicked" handler="cubie_pressed"/>
                  </object>
                  <packing>
                    <property name="left_attach">1</property>
                    <property name="right_attach">2</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkButton" id="btn-B">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                    <property name="image">img-B</property>
                    <property name="relief">none</property>
                    <property name="focus_on_click">False</property>
                  </object>
                  <packing>
                    <property name="left_attach">1</property>
                    <property name="right_attach">2</property>
                    <property name="top_attach">1</property>
                    <property name="bottom_attach">2</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkButton" id="btn-BUL">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                    <property name="image">img-BUL</property>
                    <property name="relief">none</property>
                    <property name="focus_on_click">False</property>
                    <signal name="clicked" handler="cubie_pressed"/>
                  </object>
                  <packing>
                    <property name="left_attach">2</property>
                    <property name="right_attach">3</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkButton" id="btn-BR">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                    <property name="image">img-BR</property>
                    <property name="relief">none</property>
                    <property name="focus_on_click">False</property>
                    <signal name="clicked" handler="cubie_pressed"/>
                  </object>
                  <packing>
                    <property name="top_attach">1</property>
                    <property name="bottom_attach">2</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkButton" id="btn-BL">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                    <property name="image">img-BL</property>
                    <property name="relief">none</property>
                    <property name="focus_on_click">False</property>
                    <signal name="clicked" handler="cubie_pressed"/>
                  </object>
                  <packing>
                    <property name="left_attach">2</property>
                    <property name="right_attach">3</property>
                    <property name="top_attach">1</property>
                    <property name="bottom_attach">2</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkButton" id="btn-BDR">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                    <property name="image">img-BDR</property>
                    <property name="relief">none</property>
                    <property name="focus_on_click">False</property>
                    <signal name="clicked" handler="cubie_pressed"/>
                  </object>
                  <packing>
                    <property name="top_attach">2</property>
                    <property name="bottom_attach">3</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkButton" id="btn-BD">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                    <property name="image">img-BD</property>
                    <property name="relief">none</property>
                    <property name="focus_on_click">False</property>
                    <signal name="clicked" handler="cubie_pressed"/>
                  </object>
                  <packing>
                    <property name="left_attach">1</property>
                    <property name="right_attach">2</property>
                    <property name="top_attach">2</property>
                    <property name="bottom_attach">3</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkButton" id="btn-BLD">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                    <property name="image">img-BLD</property>
                    <property name="relief">none</property>
                    <property name="focus_on_click">False</property>
                    <signal name="clicked" handler="cubie_pressed"/>
                  </object>
                  <packing>
                    <property name="left_attach">2</property>
                    <property name="right_attach">3</property>
                    <property name="top_attach">2</property>
                    <property name="bottom_attach">3</property>
                  </packing>
                </child>
              </object>
              <packing>
                <property name="left_attach">3</property>
                <property name="right_attach">4</property>
                <property name="top_attach">1</property>
                <property name="bottom_attach">2</property>
              </packing>
            </child>
            <child>
              <object class="GtkTable" id="table6">
                <property name="visible">True</property>
                <property name="n_rows">3</property>
                <property name="n_columns">3</property>
                <child>
                  <object class="GtkButton" id="btn-DLF">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                    <property name="image">img-DLF</property>
                    <property name="relief">none</property>
                    <property name="focus_on_click">False</property>
                    <signal name="clicked" handler="cubie_pressed"/>
                  </object>
                </child>
                <child>
                  <object class="GtkButton" id="btn-DL">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                    <property name="image">img-DL</property>
                    <property name="relief">none</property>
                    <property name="focus_on_click">False</property>
                    <signal name="clicked" handler="cubie_pressed"/>
                  </object>
                  <packing>
                    <property name="top_attach">1</property>
                    <property name="bottom_attach">2</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkButton" id="btn-DBL">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                    <property name="image">img-DBL</property>
                    <property name="relief">none</property>
                    <property name="focus_on_click">False</property>
                    <signal name="clicked" handler="cubie_pressed"/>
                  </object>
                  <packing>
                    <property name="top_attach">2</property>
                    <property name="bottom_attach">3</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkButton" id="btn-DF">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                    <property name="image">img-DF</property>
                    <property name="relief">none</property>
                    <property name="focus_on_click">False</property>
                    <signal name="clicked" handler="cubie_pressed"/>
                  </object>
                  <packing>
                    <property name="left_attach">1</property>
                    <property name="right_attach">2</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkButton" id="btn-D">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                    <property name="image">img-D</property>
                    <property name="relief">none</property>
                    <property name="focus_on_click">False</property>
                  </object>
                  <packing>
                    <property name="left_attach">1</property>
                    <property name="right_attach">2</property>
                    <property name="top_attach">1</property>
                    <property name="bottom_attach">2</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkButton" id="btn-DB">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                    <property name="image">img-DB</property>
                    <property name="relief">none</property>
                    <property name="focus_on_click">False</property>
                    <signal name="clicked" handler="cubie_pressed"/>
                  </object>
                  <packing>
                    <property name="left_attach">1</property>
                    <property name="right_attach">2</property>
                    <property name="top_attach">2</property>
                    <property name="bottom_attach">3</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkButton" id="btn-DFR">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                    <property name="image">img-DFR</property>
                    <property name="relief">none</property>
                    <property name="focus_on_click">False</property>
                    <signal name="clicked" handler="cubie_pressed"/>
                  </object>
                  <packing>
                    <property name="left_attach">2</property>
                    <property name="right_attach">3</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkButton" id="btn-DR">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                    <property name="image">img-DR</property>
                    <property name="relief">none</property>
                    <property name="focus_on_click">False</property>
                    <signal name="clicked" handler="cubie_pressed"/>
                  </object>
                  <packing>
                    <property name="left_attach">2</property>
                    <property name="right_attach">3</property>
                    <property name="top_attach">1</property>
                    <property name="bottom_attach">2</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkButton" id="btn-DRB">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                    <property name="image">img-DRB</property>
                    <property name="relief">none</property>
                    <property name="focus_on_click">False</property>
                    <signal name="clicked" handler="cubie_pressed"/>
                  </object>
                  <packing>
                    <property name="left_attach">2</property>
                    <property name="right_attach">3</property>
                    <property name="top_attach">2</property>
                    <property name="bottom_attach">3</property>
                  </packing>
                </child>
              </object>
              <packing>
                <property name="left_attach">1</property>
                <property name="right_attach">2</property>
                <property name="top_attach">2</property>
                <property name="bottom_attach">3</property>
              </packing>
            </child>
            <child>
              <object class="GtkTable" id="table7">
                <property name="visible">True</property>
                <property name="n_rows">3</property>
                <property name="n_columns">3</property>
                <child>
                  <object class="GtkButton" id="btn-UFL">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                    <property name="image">img-UFL</property>
                    <property name="relief">none</property>
                    <property name="focus_on_click">False</property>
                    <signal name="clicked" handler="cubie_pressed"/>
                  </object>
                  <packing>
                    <property name="top_attach">2</property>
                    <property name="bottom_attach">3</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkButton" id="btn-UF">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                    <property name="image">img-UF</property>
                    <property name="relief">none</property>
                    <property name="focus_on_click">False</property>
                    <signal name="clicked" handler="cubie_pressed"/>
                  </object>
                  <packing>
                    <property name="left_attach">1</property>
                    <property name="right_attach">2</property>
                    <property name="top_attach">2</property>
                    <property name="bottom_attach">3</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkButton" id="btn-URF">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                    <property name="image">img-URF</property>
                    <property name="relief">none</property>
                    <property name="focus_on_click">False</property>
                    <signal name="clicked" handler="cubie_pressed"/>
                  </object>
                  <packing>
                    <property name="left_attach">2</property>
                    <property name="right_attach">3</property>
                    <property name="top_attach">2</property>
                    <property name="bottom_attach">3</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkButton" id="btn-UL">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                    <property name="image">img-UL</property>
                    <property name="relief">none</property>
                    <property name="focus_on_click">False</property>
                    <signal name="clicked" handler="cubie_pressed"/>
                  </object>
                  <packing>
                    <property name="top_attach">1</property>
                    <property name="bottom_attach">2</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkButton" id="btn-ULB">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                    <property name="image">img-ULB</property>
                    <property name="relief">none</property>
                    <property name="focus_on_click">False</property>
                    <signal name="clicked" handler="cubie_pressed"/>
                  </object>
                </child>
                <child>
                  <object class="GtkButton" id="btn-U">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                    <property name="image">img-U</property>
                    <property name="relief">none</property>
                    <property name="focus_on_click">False</property>
                  </object>
                  <packing>
                    <property name="left_attach">1</property>
                    <property name="right_attach">2</property>
                    <property name="top_attach">1</property>
                    <property name="bottom_attach">2</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkButton" id="btn-UB">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                    <property name="image">img-UB</property>
                    <property name="relief">none</property>
                    <property name="focus_on_click">False</property>
                    <signal name="clicked" handler="cubie_pressed"/>
                  </object>
                  <packing>
                    <property name="left_attach">1</property>
                    <property name="right_attach">2</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkButton" id="btn-UBR">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                    <property name="image">img-UBR</property>
                    <property name="relief">none</property>
                    <property name="focus_on_click">False</property>
                    <signal name="clicked" handler="cubie_pressed"/>
                  </object>
                  <packing>
                    <property name="left_attach">2</property>
                    <property name="right_attach">3</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkButton" id="btn-UR">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                    <property name="image">img-UR</property>
                    <property name="relief">none</property>
                    <property name="focus_on_click">False</property>
                    <signal name="clicked" handler="cubie_pressed"/>
                  </object>
                  <packing>
                    <property name="left_attach">2</property>
                    <property name="right_attach">3</property>
                    <property name="top_attach">1</property>
                    <property name="bottom_attach">2</property>
                  </packing>
                </child>
              </object>
              <packing>
                <property name="left_attach">1</property>
                <property name="right_attach">2</property>
              </packing>
            </child>
            <child>
              <object class="GtkVBox" id="vbox4">
                <property name="visible">True</property>
                <property name="orientation">vertical</property>
                <child>
                  <object class="GtkAlignment" id="alignment1">
                    <property name="visible">True</property>
                    <child>
                      <placeholder/>
                    </child>
                  </object>
                  <packing>
                    <property name="position">0</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkButton" id="btn-go">
                    <property name="label" translatable="yes">Go</property>
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                    <signal name="clicked" handler="go"/>
                  </object>
                  <packing>
                    <property name="position">1</property>
                  </packing>
                </child>
              </object>
              <packing>
                <property name="left_attach">3</property>
                <property name="right_attach">4</property>
                <property name="top_attach">2</property>
                <property name="bottom_attach">3</property>
              </packing>
            </child>
            <child>
              <placeholder/>
            </child>
            <child>
              <placeholder/>
            </child>
            <child>
              <placeholder/>
            </child>
            <child>
              <placeholder/>
            </child>
            <child>
              <placeholder/>
            </child>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">False</property>
            <property name="position">1</property>
          </packing>
        </child>
        <child>
          <object class="GtkHBox" id="hbox1">
            <property name="visible">True</property>
            <child>
              <object class="GtkRadioButton" id="rad-swap">
                <property name="label" translatable="yes">Swap</property>
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="receives_default">False</property>
                <property name="focus_on_click">False</property>
                <property name="active">True</property>
                <property name="draw_indicator">True</property>
                <signal name="clicked" handler="mode_changed"/>
              </object>
              <packing>
                <property name="position">0</property>
              </packing>
            </child>
            <child>
              <object class="GtkRadioButton" id="rad-twist">
                <property name="label" translatable="yes">Twist</property>
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="receives_default">False</property>
                <property name="focus_on_click">False</property>
                <property name="draw_indicator">True</property>
                <property name="group">rad-swap</property>
                <signal name="clicked" handler="mode_changed"/>
              </object>
              <packing>
                <property name="position">1</property>
              </packing>
            </child>
            <child>
              <object class="GtkRadioButton" id="rad-pos">
                <property name="label" translatable="yes">Ignore Position (?)</property>
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="receives_default">False</property>
                <property name="focus_on_click">False</property>
                <property name="draw_indicator">True</property>
                <property name="group">rad-swap</property>
                <signal name="clicked" handler="mode_changed"/>
              </object>
              <packing>
                <property name="position">2</property>
              </packing>
            </child>
            <child>
              <object class="GtkRadioButton" id="rad-orient">
                <property name="label" translatable="yes">Ignore orientation (@)</property>
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="receives_default">False</property>
                <property name="focus_on_click">False</property>
                <property name="draw_indicator">True</property>
                <property name="group">rad-swap</property>
                <signal name="clicked" handler="mode_changed"/>
              </object>
              <packing>
                <property name="position">3</property>
              </packing>
            </child>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">False</property>
            <property name="position">2</property>
          </packing>
        </child>
        <child>
          <object class="GtkLabel" id="lbl-cubestate">
            <property name="visible">True</property>
            <property name="label" translatable="yes">UF UR UB UL DF DR DB DL FR FL BR BL UFR URB UBL ULF DRF DFL DLB DBR</property>
            <property name="selectable">True</property>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="position">3</property>
          </packing>
        </child>
        <child>
          <object class="GtkHBox" id="hbox2">
            <property name="visible">True</property>
            <child>
              <object class="GtkVBox" id="vbox2">
                <property name="visible">True</property>
                <property name="orientation">vertical</property>
                <child>
                  <object class="GtkHBox" id="hbox3">
                    <property name="visible">True</property>
                    <child>
                      <object class="GtkButton" id="btn-turn-U">
                        <property name="label" translatable="yes">U</property>
                        <property name="visible">True</property>
                        <property name="can_focus">True</property>
                        <property name="receives_default">True</property>
                        <property name="focus_on_click">False</property>
                        <signal name="clicked" handler="turn_clicked"/>
                      </object>
                      <packing>
                        <property name="position">0</property>
                      </packing>
                    </child>
                    <child>
                      <object class="GtkButton" id="btn-turn-D">
                        <property name="label" translatable="yes">D</property>
                        <property name="visible">True</property>
                        <property name="can_focus">True</property>
                        <property name="receives_default">True</property>
                        <property name="focus_on_click">False</property>
                        <signal name="clicked" handler="turn_clicked"/>
                      </object>
                      <packing>
                        <property name="position">1</property>
                      </packing>
                    </child>
                    <child>
                      <object class="GtkButton" id="btn-turn-F">
                        <property name="label" translatable="yes">F</property>
                        <property name="visible">True</property>
                        <property name="can_focus">True</property>
                        <property name="receives_default">True</property>
                        <property name="focus_on_click">False</property>
                        <signal name="clicked" handler="turn_clicked"/>
                      </object>
                      <packing>
                        <property name="position">2</property>
                      </packing>
                    </child>
                    <child>
                      <object class="GtkButton" id="btn-turn-B">
                        <property name="label" translatable="yes">B</property>
                        <property name="visible">True</property>
                        <property name="can_focus">True</property>
                        <property name="receives_default">True</property>
                        <property name="focus_on_click">False</property>
                        <signal name="clicked" handler="turn_clicked"/>
                      </object>
                      <packing>
                        <property name="position">3</property>
                      </packing>
                    </child>
                    <child>
                      <object class="GtkButton" id="btn-turn-L">
                        <property name="label" translatable="yes">L</property>
                        <property name="visible">True</property>
                        <property name="can_focus">True</property>
                        <property name="receives_default">True</property>
                        <property name="focus_on_click">False</property>
                        <signal name="clicked" handler="turn_clicked"/>
                      </object>
                      <packing>
                        <property name="position">4</property>
                      </packing>
                    </child>
                    <child>
                      <object class="GtkButton" id="btn-turn-R">
                        <property name="label" translatable="yes">R</property>
                        <property name="visible">True</property>
                        <property name="can_focus">True</property>
                        <property name="receives_default">True</property>
                        <property name="focus_on_click">False</property>
                        <signal name="clicked" handler="turn_clicked"/>
                      </object>
                      <packing>
                        <property name="position">5</property>
                      </packing>
                    </child>
                    <child>
                      <object class="GtkButton" id="btn-turn-E">
                        <property name="label" translatable="yes">E</property>
                        <property name="visible">True</property>
                        <property name="can_focus">True</property>
                        <property name="receives_default">True</property>
                        <property name="focus_on_click">False</property>
                        <signal name="clicked" handler="turn_clicked"/>
                      </object>
                      <packing>
                        <property name="position">6</property>
                      </packing>
                    </child>
                    <child>
                      <object class="GtkButton" id="btn-turn-S">
                        <property name="label" translatable="yes">S</property>
                        <property name="visible">True</property>
                        <property name="can_focus">True</property>
                        <property name="receives_default">True</property>
                        <property name="focus_on_click">False</property>
                        <signal name="clicked" handler="turn_clicked"/>
                      </object>
                      <packing>
                        <property name="position">7</property>
                      </packing>
                    </child>
                    <child>
                      <object class="GtkButton" id="btn-turn-M">
                        <property name="label" translatable="yes">M</property>
                        <property name="visible">True</property>
                        <property name="can_focus">True</property>
                        <property name="receives_default">True</property>
                        <property name="focus_on_click">False</property>
                        <signal name="clicked" handler="turn_clicked"/>
                      </object>
                      <packing>
                        <property name="position">8</property>
                      </packing>
                    </child>
                  </object>
                  <packing>
                    <property name="position">0</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkHBox" id="hbox5">
                    <property name="visible">True</property>
                    <child>
                      <object class="GtkLabel" id="label2">
                        <property name="visible">True</property>
                        <property name="tooltip_text" translatable="yes">leading and trailing moves (E, E', E2, D, D2 E', U D2 E2, ...). The possible combinations are: UDE, FBS, LRM, and their sub-strings UD, UE, DE, U, D, E, ...).</property>
                        <property name="xpad">3</property>
                        <property name="label" translatable="yes">Leading Moves:</property>
                      </object>
                      <packing>
                        <property name="position">0</property>
                      </packing>
                    </child>
                    <child>
                      <object class="GtkEntry" id="txt-leading">
                        <property name="visible">True</property>
                        <property name="can_focus">True</property>
                        <property name="invisible_char">&#x25CF;</property>
                        <property name="caps_lock_warning">False</property>
                      </object>
                      <packing>
                        <property name="position">1</property>
                      </packing>
                    </child>
                    <child>
                      <object class="GtkCheckButton" id="chk-optimal">
                        <property name="label" translatable="yes">optimal</property>
                        <property name="visible">True</property>
                        <property name="can_focus">True</property>
                        <property name="receives_default">False</property>
                        <property name="focus_on_click">False</property>
                        <property name="draw_indicator">True</property>
                        <signal name="toggled" handler="optimal_toggled"/>
                      </object>
                      <packing>
                        <property name="position">2</property>
                      </packing>
                    </child>
                  </object>
                  <packing>
                    <property name="position">1</property>
                  </packing>
                </child>
              </object>
              <packing>
                <property name="position">0</property>
              </packing>
            </child>
            <child>
              <object class="GtkVSeparator" id="vseparator1">
                <property name="visible">True</property>
                <property name="orientation">vertical</property>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="position">1</property>
              </packing>
            </child>
            <child>
              <object class="GtkHBox" id="hbox4">
                <property name="visible">True</property>
                <child>
                  <object class="GtkRadioButton" id="rad-htm">
                    <property name="label" translatable="yes">HTM</property>
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">False</property>
                    <property name="focus_on_click">False</property>
                    <property name="active">True</property>
                    <property name="draw_indicator">True</property>
                    <signal name="clicked" handler="metric_changed"/>
                  </object>
                  <packing>
                    <property name="position">0</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkRadioButton" id="rad-qtm">
                    <property name="label" translatable="yes">QTM</property>
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">False</property>
                    <property name="focus_on_click">False</property>
                    <property name="draw_indicator">True</property>
                    <property name="group">rad-htm</property>
                    <signal name="clicked" handler="metric_changed"/>
                  </object>
                  <packing>
                    <property name="position">1</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkRadioButton" id="rad-stm">
                    <property name="label" translatable="yes">STM</property>
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">False</property>
                    <property name="focus_on_click">False</property>
                    <property name="draw_indicator">True</property>
                    <property name="group">rad-htm</property>
                    <signal name="clicked" handler="metric_changed"/>
                  </object>
                  <packing>
                    <property name="position">2</property>
                  </packing>
                </child>
              </object>
              <packing>
                <property name="position">2</property>
              </packing>
            </child>
          </object>
          <packing>
            <property name="position">4</property>
          </packing>
        </child>
        <child>
          <object class="GtkHBox" id="hbox6">
            <property name="visible">True</property>
            <child>
              <placeholder/>
            </child>
            <child>
              <object class="GtkButton" id="btn-reset">
                <property name="label" translatable="yes">Reset</property>
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="receives_default">True</property>
                <signal name="clicked" handler="reset"/>
              </object>
              <packing>
                <property name="position">1</property>
              </packing>
            </child>
            <child>
              <object class="GtkButton" id="btn-exit">
                <property name="label" translatable="yes">Exit</property>
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="receives_default">True</property>
                <signal name="clicked" handler="gtk_main_quit"/>
              </object>
              <packing>
                <property name="position">2</property>
              </packing>
            </child>
          </object>
          <packing>
            <property name="position">5</property>
          </packing>
        </child>
      </object>
    </child>
  </object>
  <object class="GtkImage" id="img-FUR">
    <property name="visible">True</property>
    <property name="pixbuf">pics/green.png</property>
  </object>
  <object class="GtkImage" id="img-FL">
    <property name="visible">True</property>
    <property name="pixbuf">pics/green.png</property>
  </object>
  <object class="GtkImage" id="img-F">
    <property name="visible">True</property>
    <property name="pixbuf">pics/green.png</property>
  </object>
  <object class="GtkImage" id="img-FR">
    <property name="visible">True</property>
    <property name="pixbuf">pics/green.png</property>
  </object>
  <object class="GtkImage" id="img-FDL">
    <property name="visible">True</property>
    <property name="pixbuf">pics/green.png</property>
  </object>
  <object class="GtkImage" id="img-FD">
    <property name="visible">True</property>
    <property name="pixbuf">pics/green.png</property>
  </object>
  <object class="GtkImage" id="img-FRD">
    <property name="visible">True</property>
    <property name="pixbuf">pics/green.png</property>
  </object>
  <object class="GtkTextBuffer" id="txtbfr-out"/>
  <object class="GtkImage" id="img-FLU">
    <property name="visible">True</property>
    <property name="pixbuf">pics/green.png</property>
  </object>
  <object class="GtkImage" id="img-UFL">
    <property name="visible">True</property>
    <property name="pixbuf">pics/white.png</property>
  </object>
  <object class="GtkImage" id="img-LFD">
    <property name="visible">True</property>
    <property name="pixbuf">pics/orange.png</property>
  </object>
  <object class="GtkImage" id="img-LD">
    <property name="visible">True</property>
    <property name="pixbuf">pics/orange.png</property>
  </object>
  <object class="GtkImage" id="img-LDB">
    <property name="visible">True</property>
    <property name="pixbuf">pics/orange.png</property>
  </object>
  <object class="GtkImage" id="img-LF">
    <property name="visible">True</property>
    <property name="pixbuf">pics/orange.png</property>
  </object>
  <object class="GtkImage" id="img-L">
    <property name="visible">True</property>
    <property name="pixbuf">pics/orange.png</property>
  </object>
  <object class="GtkImage" id="img-LB">
    <property name="visible">True</property>
    <property name="pixbuf">pics/orange.png</property>
  </object>
  <object class="GtkImage" id="img-LBU">
    <property name="visible">True</property>
    <property name="pixbuf">pics/orange.png</property>
  </object>
  <object class="GtkImage" id="img-LU">
    <property name="visible">True</property>
    <property name="pixbuf">pics/orange.png</property>
  </object>
  <object class="GtkImage" id="img-LUF">
    <property name="visible">True</property>
    <property name="pixbuf">pics/orange.png</property>
  </object>
  <object class="GtkImage" id="img-UBR">
    <property name="visible">True</property>
    <property name="pixbuf">pics/white.png</property>
  </object>
  <object class="GtkImage" id="img-UB">
    <property name="visible">True</property>
    <property name="pixbuf">pics/white.png</property>
  </object>
  <object class="GtkImage" id="img-ULB">
    <property name="visible">True</property>
    <property name="pixbuf">pics/white.png</property>
  </object>
  <object class="GtkImage" id="img-UL">
    <property name="visible">True</property>
    <property name="pixbuf">pics/white.png</property>
  </object>
  <object class="GtkImage" id="img-U">
    <property name="visible">True</property>
    <property name="pixbuf">pics/white.png</property>
  </object>
  <object class="GtkImage" id="img-UF">
    <property name="visible">True</property>
    <property name="pixbuf">pics/white.png</property>
  </object>
  <object class="GtkImage" id="img-URF">
    <property name="visible">True</property>
    <property name="pixbuf">pics/white.png</property>
  </object>
  <object class="GtkImage" id="img-UR">
    <property name="visible">True</property>
    <property name="pixbuf">pics/white.png</property>
  </object>
  <object class="GtkImage" id="img-DLF">
    <property name="visible">True</property>
    <property name="pixbuf">pics/yellow.png</property>
  </object>
  <object class="GtkImage" id="img-DF">
    <property name="visible">True</property>
    <property name="pixbuf">pics/yellow.png</property>
  </object>
  <object class="GtkImage" id="img-DFR">
    <property name="visible">True</property>
    <property name="pixbuf">pics/yellow.png</property>
  </object>
  <object class="GtkImage" id="img-DL">
    <property name="visible">True</property>
    <property name="pixbuf">pics/yellow.png</property>
  </object>
  <object class="GtkImage" id="img-D">
    <property name="visible">True</property>
    <property name="pixbuf">pics/yellow.png</property>
  </object>
  <object class="GtkImage" id="img-DR">
    <property name="visible">True</property>
    <property name="pixbuf">pics/yellow.png</property>
  </object>
  <object class="GtkImage" id="img-DBL">
    <property name="visible">True</property>
    <property name="pixbuf">pics/yellow.png</property>
  </object>
  <object class="GtkImage" id="img-DB">
    <property name="visible">True</property>
    <property name="pixbuf">pics/yellow.png</property>
  </object>
  <object class="GtkImage" id="img-DRB">
    <property name="visible">True</property>
    <property name="pixbuf">pics/yellow.png</property>
  </object>
  <object class="GtkImage" id="img-RFU">
    <property name="visible">True</property>
    <property name="pixbuf">pics/red.png</property>
  </object>
  <object class="GtkImage" id="img-RF">
    <property name="visible">True</property>
    <property name="pixbuf">pics/red.png</property>
  </object>
  <object class="GtkImage" id="img-RDF">
    <property name="visible">True</property>
    <property name="pixbuf">pics/red.png</property>
  </object>
  <object class="GtkImage" id="img-RU">
    <property name="visible">True</property>
    <property name="pixbuf">pics/red.png</property>
  </object>
  <object class="GtkImage" id="img-R">
    <property name="visible">True</property>
    <property name="pixbuf">pics/red.png</property>
  </object>
  <object class="GtkImage" id="img-RD">
    <property name="visible">True</property>
    <property name="pixbuf">pics/red.png</property>
  </object>
  <object class="GtkImage" id="img-RUB">
    <property name="visible">True</property>
    <property name="pixbuf">pics/red.png</property>
  </object>
  <object class="GtkImage" id="img-RB">
    <property name="visible">True</property>
    <property name="pixbuf">pics/red.png</property>
  </object>
  <object class="GtkImage" id="img-RBD">
    <property name="visible">True</property>
    <property name="pixbuf">pics/red.png</property>
  </object>
  <object class="GtkImage" id="img-BDR">
    <property name="visible">True</property>
    <property name="pixbuf">pics/blue.png</property>
  </object>
  <object class="GtkImage" id="img-BR">
    <property name="visible">True</property>
    <property name="pixbuf">pics/blue.png</property>
  </object>
  <object class="GtkImage" id="img-BRU">
    <property name="visible">True</property>
    <property name="pixbuf">pics/blue.png</property>
  </object>
  <object class="GtkImage" id="img-BD">
    <property name="visible">True</property>
    <property name="pixbuf">pics/blue.png</property>
  </object>
  <object class="GtkImage" id="img-B">
    <property name="visible">True</property>
    <property name="pixbuf">pics/blue.png</property>
  </object>
  <object class="GtkImage" id="img-BU">
    <property name="visible">True</property>
    <property name="pixbuf">pics/blue.png</property>
  </object>
  <object class="GtkImage" id="img-BUL">
    <property name="visible">True</property>
    <property name="pixbuf">pics/blue.png</property>
  </object>
  <object class="GtkImage" id="img-BL">
    <property name="visible">True</property>
    <property name="pixbuf">pics/blue.png</property>
  </object>
  <object class="GtkImage" id="img-BLD">
    <property name="visible">True</property>
    <property name="pixbuf">pics/blue.png</property>
  </object>
  <object class="GtkImage" id="img-FU">
    <property name="visible">True</property>
    <property name="pixbuf">pics/green.png</property>
  </object>
  <object class="GtkWindow" id="win-output">
    <property name="width_request">600</property>
    <property name="height_request">400</property>
    <property name="title" translatable="yes">Alg Ouput</property>
    <property name="deletable">False</property>
    <child>
      <object class="GtkVBox" id="vbox3">
        <property name="visible">True</property>
        <property name="orientation">vertical</property>
        <child>
          <object class="GtkScrolledWindow" id="scrolledwindow1">
            <property name="visible">True</property>
            <property name="can_focus">True</property>
            <property name="hscrollbar_policy">automatic</property>
            <property name="vscrollbar_policy">automatic</property>
            <property name="shadow_type">in</property>
            <child>
              <object class="GtkTextView" id="txt-output">
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="editable">False</property>
                <property name="buffer">txtbfr-out</property>
              </object>
            </child>
          </object>
          <packing>
            <property name="position">0</property>
          </packing>
        </child>
        <child>
          <object class="GtkStatusbar" id="statusbar1">
            <property name="visible">True</property>
            <property name="spacing">2</property>
            <child>
              <object class="GtkLabel" id="label3">
                <property name="visible">True</property>
                <property name="label" translatable="yes">Output</property>
              </object>
              <packing>
                <property name="position">1</property>
              </packing>
            </child>
            <child>
              <object class="GtkButton" id="btn-close">
                <property name="label" translatable="yes">Close</property>
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="receives_default">True</property>
                <signal name="clicked" handler="window2_close"/>
              </object>
              <packing>
                <property name="position">2</property>
              </packing>
            </child>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="position">1</property>
          </packing>
        </child>
      </object>
    </child>
  </object>
</interface>
'''
class acubeProcess(ProcessProtocol):
    def __init__(self, args, gui):
        self.args=args
        self.gui = gui
    def connectionMade(self):
        self.transport.write(self.args)
    def outReceived(self, data):
        self.gui.widgets['txtbfr-out'].insert(self.gui.widgets['txtbfr-out'].get_end_iter(), data)
    def errReceived(self, data):
        line=data
        if line.find("Done.")==0:
            self.gui.widgets['txtbfr-out'].insert(self.gui.widgets['txtbfr-out'].get_end_iter(), 'Done\n')
            self.gui.go(None)
        elif line.find('depth')==0:
            self.gui.widgets['txtbfr-out'].insert(self.gui.widgets['txtbfr-out'].get_end_iter(), line)
    
class acube:
    def __init__(self):
        widget_list = [
            'win-main',
            'btn-LBU',
            'btn-LU',
            'btn-LUF',
            'btn-LB',
            'btn-L',
            'btn-LF',
            'btn-LDB',
            'btn-LD',
            'btn-LFD',
            'btn-FU',
            'btn-FUR',
            'btn-FL',
            'btn-F',
            'btn-FR',
            'btn-FDL',
            'btn-FD',
            'btn-FRD',
            'btn-FLU',
            'btn-RFU',
            'btn-RF',
            'btn-RDF',
            'btn-RU',
            'btn-R',
            'btn-RD',
            'btn-RUB',
            'btn-RB',
            'btn-RBD',
            'btn-BRU',
            'btn-BU',
            'btn-B',
            'btn-BUL',
            'btn-BR',
            'btn-BL',
            'btn-BDR',
            'btn-BD',
            'btn-BLD',
            'btn-DLF',
            'btn-DL',
            'btn-DBL',
            'btn-DF',
            'btn-D',
            'btn-DB',
            'btn-DFR',
            'btn-DR',
            'btn-DRB',
            'btn-UFL',
            'btn-UF',
            'btn-URF',
            'btn-UL',
            'btn-ULB',
            'btn-U',
            'btn-UB',
            'btn-UBR',
            'btn-UR',
            'rad-swap',
            'rad-twist',
            'rad-pos',
            'rad-orient',
            'lbl-cubestate',
            'btn-turn-U',
            'btn-turn-D',
            'btn-turn-F',
            'btn-turn-B',
            'btn-turn-L',
            'btn-turn-R',
            'btn-turn-E',
            'btn-turn-S',
            'btn-turn-M',
            'label2',
            'txt-leading',
            'rad-htm',
            'rad-qtm',
            'rad-stm',
            'btn-reset',
            'btn-go',
            'img-FUR',
            'img-FL',
            'img-F',
            'img-FR',
            'img-FDL',
            'img-FD',
            'img-FRD',
            'img-FLU',
            'img-UFL',
            'img-LFD',
            'img-LD',
            'img-LDB',
            'img-LF',
            'img-L',
            'img-LB',
            'img-LBU',
            'img-LU',
            'img-LUF',
            'img-UBR',
            'img-UB',
            'img-ULB',
            'img-UL',
            'img-U',
            'img-UF',
            'img-URF',
            'img-UR',
            'img-DLF',
            'img-DF',
            'img-DFR',
            'img-DL',
            'img-D',
            'img-DR',
            'img-DBL',
            'img-DB',
            'img-DRB',
            'img-RFU',
            'img-RF',
            'img-RDF',
            'img-RU',
            'img-R',
            'img-RD',
            'img-RUB',
            'img-RB',
            'img-RBD',
            'img-BDR',
            'img-BR',
            'img-BRU',
            'img-BD',
            'img-B',
            'img-BU',
            'img-BUL',
            'img-BL',
            'img-BLD',
            'img-FU',
            'win-output',
            'txt-output',
            'label3',
            'btn-close',
            'txtbfr-out',
            'img-green',
            'btn-exit'
            ]
            
        self.process=None
        self.running = False
        self.swapping = False
        self.swapped = ['',[],[]]
        self.mode = 0  #modes 0:swap, 1:twist, 2:?, 3:@
        self.metric = 'f'
        self.optimal = ''
        self.cube ={'LBU':['orange','ULB'],'LU':['orange','UL'], 'LUF':['orange','UFL'],'LB':['orange','BL'],'L':['orange','L'],'LF':['orange','FL'],'LDB':['orange','DBL'],'LD':['orange','DL'],'LFD':['orange','DLF'],
                    'FU':['green','UF'],'FUR':['green','URF'],'FL':['green','FL'],'F':['green','F'],'FR':['green','FR'],'FDL':['green','DLF'],'FD':['green','DF'],'FRD':['green','DFR'],'FLU':['green','UFL'],
                    'RFU':['red','URF'],'RF':['red','FR'],'RDF':['red','DFR'],'RU':['red','UR'],'R':['red','R'],'RD':['red','DR'],'RUB':['red','UBR'],'RB':['red','BR'],'RBD':['red','DRB'],
                    'BRU':['blue','UBR'],'BU':['blue','UB'],'B':['blue','B'],'BUL':['blue','ULB'],'BR':['blue','BR'],'BL':['blue','BL'],'BDR':['blue','DRB'],'BD':['blue','DB'],'BLD':['blue','DBL'],
                    'DLF':['yellow','DLF'],'DL':['yellow','DL'],'DBL':['yellow','DBL'],'DF':['yellow','DF'],'D':['yellow','D'],'DB':['yellow','DB'],'DFR':['yellow','DFR'],'DR':['yellow','DR'],'DRB':['yellow','DRB'],
                    'UFL':['white','UFL'],'UF':['white','UF'],'URF':['white','URF'],'UL':['white','UL'],'ULB':['white','ULB'],'U':['white','U'],'UB':['white','UB'],'UBR':['white','UBR'],'UR':['white','UR']}
        self.turns = {"U":1, "D":1, "F":1, "B":1, "L":1, "R":1, "E":1, "S":1, "M":1}
        self.cubestate = {'UF':['UF',0],'UR':['UR',0],'UB':['UB',0],'UL':['UL',0],'DF':['DF',0],'DR':['DR',0],'DB':['DB',0],'DL':['DL',0],'FR':['FR',0],'FL':['FL',0],'BR':['BR',0],'BL':['BL',0],'URF':['UFR',0],'UBR':['URB',0],'UFL':['ULF',0],'ULB':['UBL',0],'DFR':['DRF',0],'DLF':['DFL',0],'DBL':['DLB',0],'DRB':['DBR',0]}
        #states: 0=o, 1=?, 2=@, 3=@?, 4=-, 5=+, 6=-?, 7=+?
        builder = gtk.Builder()
        #builder.add_from_file("acube.glade")
        builder.add_from_string(gui)
        builder.connect_signals(self)
        
        self.widgets={}
        for widget in widget_list:
            self.widgets[widget]=builder.get_object(widget)
        self.window = self.widgets["win-main"]
       
    def mode_changed(self, widget, data=None):
        if widget.get_name()=='rad-swap':
            self.mode=0
        elif widget.get_name()=='rad-twist':
            self.mode=1
        elif widget.get_name()=='rad-pos':
            self.mode=2
        else:
            self.mode=3
    def metric_changed(self, widget, data=None):
        if widget.get_name()=='rad-stm':
            self.metric='s'
        elif widget.get_name()=='rad-qtm':
            self.metric='q'
        else:
            self.metric='f'
    def optimal_toggled(self, widget, data=None):
        if self.optimal=='o':
            self.optimal=''
        else:
            self.optimal='o'
    def cubie_pressed(self, widget, data=None):
        if self.mode==0:
            self.swap(widget, data)
        else:
            self.swap_reset(widget,data)
            if self.mode==1:
                self.twist(widget, data)
            elif self.mode==2:
                self.pos(widget, data)
            else:
                self.orient(widget, data)
        self.update_cubestate(widget, data)
    def swap_reset(self, widget, data=None):
        self.swapping=False
        for btn in self.swapped[2]:
            btn.set_relief(gtk.RELIEF_NONE)
        self.swapped=['',[],[]]
        
    def sticker_swap(self, a, b):
        temp=self.cube[a][0]
        self.cube[a][0]=self.cube[b][0]
        self.cube[b][0]=temp
    def swap(self, widget, data=None):
        piece=widget.get_name().replace('btn-','')
        posit=self.cube[piece][1]
        if self.swapping:
            if posit == self.swapped[0]:
                self.swap_reset(widget,data)
            if len(piece) == len(self.swapped[0]):
                if len(piece)==2:
                    for i in self.swapped[2]:
                        i.set_relief(gtk.RELIEF_NONE)
                    temp=self.cubestate[self.swapped[0]]
                    self.cubestate[self.swapped[0]]=self.cubestate[posit]
                    self.cubestate[posit]=temp
                    stickers=[posit,posit[::-1]]
                    for i in range(2):
                        self.sticker_swap(stickers[i],self.swapped[1][i])
                    buttons=[self.widgets['btn-%s' % posit],
                             self.widgets['btn-%s' % posit[::-1]]]
                    buttons+=self.swapped[2]
                    stickers+=self.swapped[1]
                elif len(piece)==3:
                    for i in self.swapped[2]:
                        i.set_relief(gtk.RELIEF_NONE)
                    temp=self.cubestate[self.swapped[0]]
                    self.cubestate[self.swapped[0]]=self.cubestate[posit]
                    self.cubestate[posit]=temp
                    stickers=[posit,posit[2:]+posit[:2],posit[1:]+posit[:1]]
                    for i in range(3):
                        self.sticker_swap(stickers[i],self.swapped[1][i])
                    buttons=[self.widgets['btn-%s' % posit],
                             self.widgets['btn-%s' % posit[2:]+posit[:2]],
                             self.widgets['btn-%s' % posit[1:]+posit[:1]]]
                    buttons+=self.swapped[2]
                    stickers+=self.swapped[1]
                for i in range(len(buttons)):
                    state=self.cubestate[self.cube[stickers[i]][1]][1]
                    if state==1:
                        buttons[i].get_property("image").set_from_file('pics/?.png')
                    elif state==2:
                        buttons[i].get_property("image").set_from_file('pics/%s@.png' % self.cube[stickers[i]][0])
                    elif state==3:
                        buttons[i].get_property("image").set_from_file('pics/@?.png')                            
                    elif state==6:
                        buttons[i].get_property("image").set_from_file('pics/-?.png')
                    elif state==7:
                        buttons[i].get_property("image").set_from_file('pics/+?.png')
                    else:
                        buttons[i].get_property("image").set_from_file('pics/%s.png' % self.cube[stickers[i]][0])     
                self.swapped[2]=buttons
                self.swap_reset(widget, data)
        else:
            if len(piece)==2:
                piece_=self.widgets['btn-%s' % piece[::-1]]
                widget.set_relief(gtk.RELIEF_NORMAL)
                piece_.set_relief(gtk.RELIEF_NORMAL)
                sticker=self.cube[piece][1]
                self.swapped=[sticker,
                             [posit,posit[::-1]],
                             [self.widgets['btn-%s' % posit],self.widgets['btn-%s' % posit[::-1]]]]
                self.swapping=True
            elif len(piece)==3:
                piece_=self.widgets['btn-%s' % piece[1:]+piece[:1]]
                piece__=self.widgets['btn-%s' % piece[2:]+piece[:2]]
                widget.set_relief(gtk.RELIEF_NORMAL)
                piece_.set_relief(gtk.RELIEF_NORMAL)
                piece__.set_relief(gtk.RELIEF_NORMAL)
                sticker=self.cube[piece][1]
                self.swapped=[sticker,
                             [posit,posit[2:]+posit[:2],posit[1:]+posit[:1]],
                             [self.widgets['btn-%s' % posit],
                               self.widgets['btn-%s' % posit[2:]+posit[:2]],
                               self.widgets['btn-%s' % posit[1:]+posit[:1]]]]
                self.swapping=True
    def twist_edge(self,a,b):
        piece=self.cube[a][1]
        self.cubestate[piece][0]=self.cubestate[piece][0][::-1]
        temp=self.cube[a][0]
        self.cube[a][0]=self.cube[b][0]
        self.cube[b][0]=temp
    def twist_corner(self,a, b, c):
        piece=self.cube[a][1]
        self.cubestate[piece][0]=self.cubestate[piece][0][1:]+self.cubestate[piece][0][:1]
        temp=self.cube[a][0]
        self.cube[a][0]=self.cube[c][0]
        self.cube[c][0]=self.cube[b][0]
        self.cube[b][0]=temp
    def twist(self, widget, data=None):
        piece=widget.get_name().replace('btn-','')
        state=self.cubestate[self.cube[piece][1]][1]
        if len(piece)==2:  #edge
            piece_=self.widgets['btn-%s' % piece[::-1]]
            if state==0: #oriented -> -
                self.twist_edge(piece, piece[::-1])
                widget.get_property("image").set_from_file('pics/%s.png' % self.cube[piece][0])
                piece_.get_property("image").set_from_file('pics/%s.png' % self.cube[piece[::-1]][0])
                self.cubestate[self.cube[piece][1]][1]=4
            elif state==1: #? -> -?
                widget.get_property("image").set_from_file('pics/-?.png')
                piece_.get_property("image").set_from_file('pics/-?.png')
                self.cubestate[self.cube[piece][1]][1]=6
            elif state==4 or state==2: #- -> oriented
                self.twist_edge(piece, piece[::-1])
                widget.get_property("image").set_from_file('pics/%s.png' % self.cube[piece][0])
                piece_.get_property("image").set_from_file('pics/%s.png' % self.cube[piece[::-1]][0])
                self.cubestate[self.cube[piece][1]][1]=0
            elif state==6 or state==3: #-? -> ?
                widget.get_property("image").set_from_file('pics/?.png')
                piece_.get_property("image").set_from_file('pics/?.png')
                self.cubestate[self.cube[piece][1]][1]=1
        elif len(piece)==3:  #corner
            piece_=self.widgets['btn-%s' % piece[1:]+piece[:1]]
            piece__=self.widgets['btn-%s' % piece[2:]+piece[:2]]
            if state==0: #oriented -> +
                self.twist_corner(piece, piece[1:]+piece[:1], piece[2:]+piece[:2])
                widget.get_property("image").set_from_file('pics/%s.png' % self.cube[piece][0])
                piece_.get_property("image").set_from_file('pics/%s.png' % self.cube[piece[1:]+piece[:1]][0])
                piece__.get_property("image").set_from_file('pics/%s.png' % self.cube[piece[2:]+piece[:2]][0])
                self.cubestate[self.cube[piece][1]][1]=5
            elif state==1: #? -> +?
                widget.get_property("image").set_from_file('pics/+?.png')
                piece_.get_property("image").set_from_file('pics/+?.png')
                piece__.get_property("image").set_from_file('pics/+?.png')
                self.cubestate[self.cube[piece][1]][1]=7
            elif state==4 or state==2: #- -> oriented
                self.twist_corner(piece, piece[1:]+piece[:1], piece[2:]+piece[:2])
                widget.get_property("image").set_from_file('pics/%s.png' % self.cube[piece][0])
                piece_.get_property("image").set_from_file('pics/%s.png' % self.cube[piece[1:]+piece[:1]][0])
                piece__.get_property("image").set_from_file('pics/%s.png' % self.cube[piece[2:]+piece[:2]][0])
                self.cubestate[self.cube[piece][1]][1]=0 
            elif state==5: #+ -> -
                self.twist_corner(piece, piece[1:]+piece[:1], piece[2:]+piece[:2])
                widget.get_property("image").set_from_file('pics/%s.png' % self.cube[piece][0])
                piece_.get_property("image").set_from_file('pics/%s.png' % self.cube[piece[1:]+piece[:1]][0])
                piece__.get_property("image").set_from_file('pics/%s.png' % self.cube[piece[2:]+piece[:2]][0])
                self.cubestate[self.cube[piece][1]][1]=4
            elif state==6 or state==3: #-? -> ?
                widget.get_property("image").set_from_file('pics/?.png')
                piece_.get_property("image").set_from_file('pics/?.png')
                piece__.get_property("image").set_from_file('pics/?.png')
                self.cubestate[self.cube[piece][1]][1]=1
            elif state==7: #+? -> -?
                widget.get_property("image").set_from_file('pics/-?.png')
                piece_.get_property("image").set_from_file('pics/-?.png')
                piece__.get_property("image").set_from_file('pics/-?.png')
                self.cubestate[self.cube[piece][1]][1]=6 
    def pos(self, widget, data=None):
        piece=widget.get_name().replace('btn-','')
        state=self.cubestate[self.cube[piece][1]][1]
        if len(piece)==2:  #edge
            piece_=self.widgets['btn-%s' % piece[::-1]]
            if state==1:
                widget.get_property("image").set_from_file('pics/%s.png' % self.cube[piece][0])
                piece_.get_property("image").set_from_file('pics/%s.png' % self.cube[piece[::-1]][0])
                self.cubestate[self.cube[piece][1]][1]=0
            elif state==2:
                widget.get_property("image").set_from_file('pics/@?.png')
                piece_.get_property("image").set_from_file('pics/@?.png')
                self.cubestate[self.cube[piece][1]][1]=3
            elif state==3:
                widget.get_property("image").set_from_file('pics/%s@.png' % self.cube[piece][0])
                piece_.get_property("image").set_from_file('pics/%s@.png' % self.cube[piece[::-1]][0])
                self.cubestate[self.cube[piece][1]][1]=2
            elif state==6:
                widget.get_property("image").set_from_file('pics/%s.png' % self.cube[piece][0])
                piece_.get_property("image").set_from_file('pics/%s.png' % self.cube[piece[::-1]][0])
                self.cubestate[self.cube[piece][1]][1]=4
            elif state==4: #- -> -?
                widget.get_property("image").set_from_file('pics/-?.png')
                piece_.get_property("image").set_from_file('pics/-?.png')
                self.cubestate[self.cube[piece][1]][1]=6
            else:
                widget.get_property("image").set_from_file('pics/?.png')
                piece_.get_property("image").set_from_file('pics/?.png')
                self.cubestate[self.cube[piece][1]][1]=1
        elif len(piece)==3:  #corner
            piece_=self.widgets['btn-%s' % piece[1:]+piece[:1]]
            piece__=self.widgets['btn-%s' % piece[2:]+piece[:2]]
            if state==1:
                widget.get_property("image").set_from_file('pics/%s.png' % self.cube[piece][0])
                piece_.get_property("image").set_from_file('pics/%s.png' % self.cube[piece[1:]+piece[:1]][0])
                piece__.get_property("image").set_from_file('pics/%s.png' % self.cube[piece[2:]+piece[:2]][0])
                self.cubestate[self.cube[piece][1]][1]=0
            elif state==2:
                widget.get_property("image").set_from_file('pics/@?.png')
                piece_.get_property("image").set_from_file('pics/@?.png')
                piece__.get_property("image").set_from_file('pics/@?.png')
                self.cubestate[self.cube[piece][1]][1]=3
            elif state==3:
                widget.get_property("image").set_from_file('pics/%s@.png' % self.cube[piece][0])
                piece_.get_property("image").set_from_file('pics/%s@.png' % self.cube[piece[1:]+piece[:1]][0])
                piece__.get_property("image").set_from_file('pics/%s@.png' % self.cube[piece[2:]+piece[:2]][0])
                self.cubestate[self.cube[piece][1]][1]=2
            elif state==6:
                widget.get_property("image").set_from_file('pics/%s.png' % self.cube[piece][0])
                piece_.get_property("image").set_from_file('pics/%s.png' % self.cube[piece[1:]+piece[:1]][0])
                piece__.get_property("image").set_from_file('pics/%s.png' % self.cube[piece[2:]+piece[:2]][0])
                self.cubestate[self.cube[piece][1]][1]=4
            elif state==7:
                widget.get_property("image").set_from_file('pics/%s.png' % self.cube[piece][0])
                piece_.get_property("image").set_from_file('pics/%s.png' % self.cube[piece[1:]+piece[:1]][0])
                piece__.get_property("image").set_from_file('pics/%s.png' % self.cube[piece[2:]+piece[:2]][0])
                self.cubestate[self.cube[piece][1]][1]=5
            elif state==4:
                widget.get_property("image").set_from_file('pics/-?.png')
                piece_.get_property("image").set_from_file('pics/-?.png')
                piece__.get_property("image").set_from_file('pics/-?.png')
                self.cubestate[self.cube[piece][1]][1]=6
            elif state==5:
                widget.get_property("image").set_from_file('pics/+?.png')
                piece_.get_property("image").set_from_file('pics/+?.png')
                piece__.get_property("image").set_from_file('pics/+?.png')
                self.cubestate[self.cube[piece][1]][1]=7
            else:
                widget.get_property("image").set_from_file('pics/?.png')
                piece_.get_property("image").set_from_file('pics/?.png')
                piece__.get_property("image").set_from_file('pics/?.png')
                self.cubestate[self.cube[piece][1]][1]=1
            
    def orient(self, widget, data=None):
        piece=widget.get_name().replace('btn-','')
        state=self.cubestate[self.cube[piece][1]][1]
        if len(piece)==2:  #edge
            piece_=self.widgets['btn-%s' % piece[::-1]]
            if state==2:
                widget.get_property("image").set_from_file('pics/%s.png' % self.cube[piece][0])
                piece_.get_property("image").set_from_file('pics/%s.png' % self.cube[piece[::-1]][0])
                self.cubestate[self.cube[piece][1]][1]=0
            elif state==1:
                widget.get_property("image").set_from_file('pics/@?.png')
                piece_.get_property("image").set_from_file('pics/@?.png')
                self.cubestate[self.cube[piece][1]][1]=3
            elif state==3:
                widget.get_property("image").set_from_file('pics/?.png')
                piece_.get_property("image").set_from_file('pics/?.png')
                self.cubestate[self.cube[piece][1]][1]=1
            else:
                widget.get_property("image").set_from_file('pics/%s@.png' % self.cube[piece][0])
                piece_.get_property("image").set_from_file('pics/%s@.png' % self.cube[piece[::-1]][0])
                self.cubestate[self.cube[piece][1]][1]=2
        elif len(piece)==3:  #corner
            piece_=self.widgets['btn-%s' % piece[1:]+piece[:1]]
            piece__=self.widgets['btn-%s' % piece[2:]+piece[:2]]
            if state==2:
                widget.get_property("image").set_from_file('pics/%s.png' % self.cube[piece][0])
                piece_.get_property("image").set_from_file('pics/%s.png' % self.cube[piece[1:]+piece[:1]][0])
                piece__.get_property("image").set_from_file('pics/%s.png' % self.cube[piece[2:]+piece[:2]][0])
                self.cubestate[self.cube[piece][1]][1]=0
            elif state in [1,6,7]:
                widget.get_property("image").set_from_file('pics/@?.png')
                piece_.get_property("image").set_from_file('pics/@?.png')
                piece__.get_property("image").set_from_file('pics/@?.png')
                self.cubestate[self.cube[piece][1]][1]=3
            elif state==3:
                widget.get_property("image").set_from_file('pics/?.png')
                piece_.get_property("image").set_from_file('pics/?.png')
                piece__.get_property("image").set_from_file('pics/?.png')
                self.cubestate[self.cube[piece][1]][1]=1
            else:
                widget.get_property("image").set_from_file('pics/%s@.png' % self.cube[piece][0])
                piece_.get_property("image").set_from_file('pics/%s@.png' % self.cube[piece[1:]+piece[:1]][0])
                piece__.get_property("image").set_from_file('pics/%s@.png' % self.cube[piece[2:]+piece[:2]][0])
                self.cubestate[self.cube[piece][1]][1]=2

    def update_cubestate(self, widget, data=None):
        pieces=[self.cubestate['UF'][0],
                self.cubestate['UR'][0],
                self.cubestate['UB'][0],
                self.cubestate['UL'][0],
                self.cubestate['DF'][0],
                self.cubestate['DR'][0],
                self.cubestate['DB'][0],
                self.cubestate['DL'][0],
                self.cubestate['FR'][0],
                self.cubestate['FL'][0],
                self.cubestate['BR'][0],
                self.cubestate['BL'][0],
                self.cubestate['URF'][0],
                self.cubestate['UBR'][0],
                self.cubestate['ULB'][0],
                self.cubestate['UFL'][0],
                self.cubestate['DFR'][0],
                self.cubestate['DLF'][0],
                self.cubestate['DBL'][0],
                self.cubestate['DRB'][0]]
        states=[self.cubestate['UF'][1],
                self.cubestate['UR'][1],
                self.cubestate['UB'][1],
                self.cubestate['UL'][1],
                self.cubestate['DF'][1],
                self.cubestate['DR'][1],
                self.cubestate['DB'][1],
                self.cubestate['DL'][1],
                self.cubestate['FR'][1],
                self.cubestate['FL'][1],
                self.cubestate['BR'][1],
                self.cubestate['BL'][1],
                self.cubestate['URF'][1],
                self.cubestate['UBR'][1],
                self.cubestate['ULB'][1],
                self.cubestate['UFL'][1],
                self.cubestate['DFR'][1],
                self.cubestate['DLF'][1],
                self.cubestate['DBL'][1],
                self.cubestate['DRB'][1]]
        cubestate=[]
        #states: 0=o, 1=?, 2=@, 3=@?, 4=-, 5=+, 6=-?, 7=+?
        for i in range(20):
            if states[i]==1:
                cubestate.append('?')
            elif states[i]==2:
                cubestate.append('@'+pieces[i])
            elif states[i]==3:
                cubestate.append('@?')
            #~ elif states[i]==4:
                #~ cubestate.append(pieces[i][1:]+pieces[i][:1])
            #~ elif states[i]==5:
                #~ cubestate.append(pieces[i][2:]+pieces[i][:2])
            elif states[i]==6:
                cubestate.append('-?')
            elif states[i]==7:
                cubestate.append('+?')
            else:
                cubestate.append(pieces[i])
        self.widgets['lbl-cubestate'].set_text(' '.join(cubestate))
    def turn_clicked(self, widget, data=None):
        turn = widget.get_name().replace('btn-turn-','')
        self.turns[turn]+=1
        if self.turns[turn]==3:   self.turns[turn]=0
        
        if self.turns[turn]==0:
            widget.set_label('No %s' % turn)
        elif self.turns[turn]==1:
            widget.set_label(turn)
        elif self.turns[turn]==2:
            widget.set_label("%s2" % turn)
        
    def reset(self, widget, data=None):
        self.swap_reset(widget, data)
        self.running = False
        self.swapping = False
        self.swapped = ['',[],[]]
        self.mode = 0  #modes 0:swap, 1:twist, 2:?, 3:@
        self.cube ={'LBU':['orange','ULB'],'LU':['orange','UL'], 'LUF':['orange','UFL'],'LB':['orange','BL'],'L':['orange','L'],'LF':['orange','FL'],'LDB':['orange','DBL'],'LD':['orange','DL'],'LFD':['orange','DLF'],
                    'FU':['green','UF'],'FUR':['green','URF'],'FL':['green','FL'],'F':['green','F'],'FR':['green','FR'],'FDL':['green','DLF'],'FD':['green','DF'],'FRD':['green','DFR'],'FLU':['green','UFL'],
                    'RFU':['red','URF'],'RF':['red','FR'],'RDF':['red','DFR'],'RU':['red','UR'],'R':['red','R'],'RD':['red','DR'],'RUB':['red','UBR'],'RB':['red','BR'],'RBD':['red','DRB'],
                    'BRU':['blue','UBR'],'BU':['blue','UB'],'B':['blue','B'],'BUL':['blue','ULB'],'BR':['blue','BR'],'BL':['blue','BL'],'BDR':['blue','DRB'],'BD':['blue','DB'],'BLD':['blue','DBL'],
                    'DLF':['yellow','DLF'],'DL':['yellow','DL'],'DBL':['yellow','DBL'],'DF':['yellow','DF'],'D':['yellow','D'],'DB':['yellow','DB'],'DFR':['yellow','DFR'],'DR':['yellow','DR'],'DRB':['yellow','DRB'],
                    'UFL':['white','UFL'],'UF':['white','UF'],'URF':['white','URF'],'UL':['white','UL'],'ULB':['white','ULB'],'U':['white','U'],'UB':['white','UB'],'UBR':['white','UBR'],'UR':['white','UR']}
        self.turns = {"U":1, "D":1, "F":1, "B":1, "L":1, "R":1, "E":1, "S":1, "M":1}
        self.cubestate = {'UF':['UF',0],'UR':['UR',0],'UB':['UB',0],'UL':['UL',0],'DF':['DF',0],'DR':['DR',0],'DB':['DB',0],'DL':['DL',0],'FR':['FR',0],'FL':['FL',0],'BR':['BR',0],'BL':['BL',0],'URF':['UFR',0],'UBR':['URB',0],'UFL':['ULF',0],'ULB':['UBL',0],'DFR':['DRF',0],'DLF':['DFL',0],'DBL':['DLB',0],'DRB':['DBR',0]}
        for k,v in self.widgets.iteritems():
                sticker=k.replace('btn-','')
                if sticker in self.cube:
                    v.get_image().set_from_file('pics/%s.png' % self.cube[sticker][0])
                if 'turn-' in sticker:
                    v.set_label(sticker.replace('turn-',''))
        self.widgets['rad-htm'].clicked()
        self.widgets['rad-swap'].clicked()
        
    def gtk_main_quit(self, widget, data=None):
        gtk.main_quit()
        
    def on_window1_remove(self, widget,data=None):
        gtk.main_quit()
        
    def window2_close(self, widget, data=None):
        self.widgets['win-output'].hide_all()
        if self.running:
            self.go(widget, data)
            
    def go(self, widget, data=None):
        if self.running:
            self.widgets['btn-go'].set_label("Go")
            self.running = False
            if self.process:
                self.process.transport.signalProcess('KILL')
                #~ self.process.terminate()
                #~ self.process.wait()
                self.process=None
        else:
            self.widgets['btn-go'].set_label("Stop")
            self.widgets['txtbfr-out'].set_text('')
            self.widgets['win-output'].show_all()
            self.running = True
            self.widgets['txtbfr-out'].set_text('Searching...\n')
            self.run_acube()
            #~ process = subprocess.Popen(['java','-cp','ACube3.jar','ACube','o'], shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            #~ process.stdin.write('UF UL UB UR DF DR DB DL FR FL BR BL URB UFR UBL ULF DRF DFL DLB DBR\n')
    def get_turnmask(self):
        turns='UDFBLRESM'; hbin=''; qbin=''
        for i in turns:
            if self.turns[i]==0:
                hbin+='0'; qbin+='0'
            elif self.turns[i]==2:
                hbin+='1'; qbin+='0'
            else:
                qbin+='1';hbin+='0'
        hbin=str(int(hbin[:3],2))+str(int(hbin[3:6],2))+str(int(hbin[6:],2))
        qbin=str(int(qbin[:3],2))+str(int(qbin[3:6],2))+str(int(qbin[6:],2))
        s=''
        if hbin!='000':
            s+=qbin+hbin
        elif qbin!='000':
            s+=qbin
        if s=='777':
            s=''
        return s
    def run_acube(self):
        turnmask = self.get_turnmask()
        self.process = acubeProcess('%s %s %s\n'%(self.widgets['txt-leading'].get_text(),turnmask,self.widgets['lbl-cubestate'].get_text()), self)
        reactor.spawnProcess(self.process, 'java', ['java','-cp','ACube3.jar','ACube',self.optimal,'a',self.metric], env=os.environ)
        #~ self.process = subprocess.Popen(['java','-cp','ACube3.jar','ACube',self.optimal,'a',self.metric], shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        #~ self.process.stdin.write('%s %s %s\n'%(self.widgets['txt-leading'].get_text(),turnmask,self.widgets['lbl-cubestate'].get_text()))
        #~ stdout_id = gobject.io_add_watch(self.process.stdout, gobject.IO_IN, self.get_algs)
        #~ stderr_id = gobject.io_add_watch(self.process.stderr, gobject.IO_IN, self.print_out)

    def print_out(self, source, cb):
        line = source.readline()
        #~ print line.strip('\n')
        if line.find("Done.")==0:
            self.widgets['txtbfr-out'].insert(self.widgets['txtbfr-out'].get_end_iter(), 'Done\n')
            self.go(None)
            return False
        elif line.find('depth')==0:
            self.widgets['txtbfr-out'].insert(self.widgets['txtbfr-out'].get_end_iter(), line)
        return True
    
    def get_algs(self, source, cb):
        self.widgets['txtbfr-out'].insert(self.widgets['txtbfr-out'].get_end_iter(), source.readline())
        return True
        
if __name__ == "__main__":
    foo=acube()
    foo.window.show()
    #~ gtk.main()
    reactor.run()
