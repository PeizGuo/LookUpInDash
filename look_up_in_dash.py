import sublime, sublime_plugin
import subprocess
import re
class LookUpInDashCommand(sublime_plugin.TextCommand):
  def run(self, view):
    sels = self.view.sel()
    length = len(sels)
    if length > 0:
      region = sels[0]
      if region.empty():
        region = self.view.word(region)
      if not region.empty():
        s = self.view.substr(region)
        s = s.strip()
        if len(s) > 0:
          subprocess.call(['open', 'dash://' + self.get_prefix() + s])

  def get_prefix(self):
    file_name = self.view.file_name()
    extension = re.compile("\.(\w+)$").findall(file_name)
    if len(extension) != 0:
      return {
        "css": "css:",
        "js": "javascript:",
        "html": "html:",
        "rb": "ruby:"
      }.get(extension[0].lower(), "")
    else:
      return ''
