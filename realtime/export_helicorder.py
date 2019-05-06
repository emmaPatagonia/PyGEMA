# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) Diego Gonzalez-Vidal <diegogonzalezvidal@gmail.com>
#
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with This program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

from obspy.core import UTCDateTime
from pygema.core.parameters import load_station_metadata
from pygema.signal.read import get_streams_gema
from pygema.signal.preprocessing import remove_instrument_response
from pygema.plot.waveforms import plot_helicorder
import subprocess, time, glob, os

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

networks, stations, stlons, stlats, stalts = load_station_metadata()

savedir = "web/PyGema_Web/PyGema_Web/static/figs_html"

deadtime = 5
while True:
  this_day = UTCDateTime().now()
  starttime = UTCDateTime(this_day.strftime("%Y-%m-%d"))
  endtime = starttime + 86400.
  for network,station in zip(networks,stations):
    try:
      if network=="GM":
        st, gaps = get_streams_gema([network], [station], starttime, endtime, only_vertical_channel=True, local_dir_name=None)
        if len(st)>0:
          for tr in st:
            try:
              tr = remove_instrument_response(tr, pre_filt=(0.01, 0.02, 50, 100), detrend=True, taper=False, dataless_file=None)
              tr.filter("bandpass", freqmin=1, freqmax=10, corners=2)
            except:
              st.remove(tr)
              continue

          plot_helicorder(st, include_events_pygemadb=True, include_last_update_title=True, dark_background=True, show_plot=False, savedir=savedir)

    except:
      continue

  time.sleep(deadtime)



