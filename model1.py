{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "4df303ce",
   "metadata": {},
   "source": [
    "# intialization of libraries"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8ab730a6",
   "metadata": {},
   "source": [
    "### LangChain is a framework for developing applications powered by language models. We believe that the most powerful and differentiated applications will not only call out to a language model, but will also be:\n",
    "\n",
    "#### Data-aware: connect a language model to other sources of data\n",
    "\n",
    "#### Agentic: allow a language model to interact with its environment "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "9be52ac1",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Collecting langchain\n",
      "Note: you may need to restart the kernel to use updated packages.  Downloading langchain-0.0.190-py3-none-any.whl (983 kB)\n",
      "\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "  WARNING: The scripts langchain-server.exe and langchain.exe are installed in 'C:\\Users\\saija\\AppData\\Roaming\\Python\\Python39\\Scripts' which is not on PATH.\n",
      "  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.\n",
      "\n",
      "[notice] A new release of pip available: 22.2.2 -> 23.1.2\n",
      "[notice] To update, run: python.exe -m pip install --upgrade pip\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "     -------------------------------------- 983.2/983.2 kB 6.9 MB/s eta 0:00:00\n",
      "Collecting pydantic<2,>=1\n",
      "  Downloading pydantic-1.10.8-cp39-cp39-win_amd64.whl (2.2 MB)\n",
      "     ---------------------------------------- 2.2/2.2 MB 8.7 MB/s eta 0:00:00\n",
      "Requirement already satisfied: async-timeout<5.0.0,>=4.0.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from langchain) (4.0.1)\n",
      "Requirement already satisfied: numpy<2,>=1 in c:\\programdata\\anaconda3\\lib\\site-packages (from langchain) (1.21.5)\n",
      "Collecting openapi-schema-pydantic<2.0,>=1.2\n",
      "  Downloading openapi_schema_pydantic-1.2.4-py3-none-any.whl (90 kB)\n",
      "     ---------------------------------------- 90.0/90.0 kB ? eta 0:00:00\n",
      "Requirement already satisfied: SQLAlchemy<3,>=1.4 in c:\\programdata\\anaconda3\\lib\\site-packages (from langchain) (1.4.32)\n",
      "Collecting dataclasses-json<0.6.0,>=0.5.7\n",
      "  Downloading dataclasses_json-0.5.7-py3-none-any.whl (25 kB)\n",
      "Collecting aiohttp<4.0.0,>=3.8.3\n",
      "  Downloading aiohttp-3.8.4-cp39-cp39-win_amd64.whl (323 kB)\n",
      "     -------------------------------------- 323.6/323.6 kB 6.7 MB/s eta 0:00:00\n",
      "Requirement already satisfied: requests<3,>=2 in c:\\programdata\\anaconda3\\lib\\site-packages (from langchain) (2.27.1)\n",
      "Collecting numexpr<3.0.0,>=2.8.4\n",
      "  Downloading numexpr-2.8.4-cp39-cp39-win_amd64.whl (92 kB)\n",
      "     ---------------------------------------- 92.7/92.7 kB 2.7 MB/s eta 0:00:00\n",
      "Requirement already satisfied: PyYAML>=5.4.1 in c:\\programdata\\anaconda3\\lib\\site-packages (from langchain) (6.0)\n",
      "Collecting tenacity<9.0.0,>=8.1.0\n",
      "  Downloading tenacity-8.2.2-py3-none-any.whl (24 kB)\n",
      "Requirement already satisfied: charset-normalizer<4.0,>=2.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from aiohttp<4.0.0,>=3.8.3->langchain) (2.0.4)\n",
      "Requirement already satisfied: multidict<7.0,>=4.5 in c:\\programdata\\anaconda3\\lib\\site-packages (from aiohttp<4.0.0,>=3.8.3->langchain) (5.1.0)\n",
      "Requirement already satisfied: attrs>=17.3.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from aiohttp<4.0.0,>=3.8.3->langchain) (21.4.0)\n",
      "Requirement already satisfied: frozenlist>=1.1.1 in c:\\programdata\\anaconda3\\lib\\site-packages (from aiohttp<4.0.0,>=3.8.3->langchain) (1.2.0)\n",
      "Requirement already satisfied: aiosignal>=1.1.2 in c:\\programdata\\anaconda3\\lib\\site-packages (from aiohttp<4.0.0,>=3.8.3->langchain) (1.2.0)\n",
      "Requirement already satisfied: yarl<2.0,>=1.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from aiohttp<4.0.0,>=3.8.3->langchain) (1.6.3)\n",
      "Requirement already satisfied: typing-extensions>=3.6.5 in c:\\programdata\\anaconda3\\lib\\site-packages (from async-timeout<5.0.0,>=4.0.0->langchain) (4.1.1)\n",
      "Collecting marshmallow<4.0.0,>=3.3.0\n",
      "  Downloading marshmallow-3.19.0-py3-none-any.whl (49 kB)\n",
      "     ---------------------------------------- 49.1/49.1 kB 2.4 MB/s eta 0:00:00\n",
      "Collecting typing-inspect>=0.4.0\n",
      "  Downloading typing_inspect-0.9.0-py3-none-any.whl (8.8 kB)\n",
      "Collecting marshmallow-enum<2.0.0,>=1.5.1\n",
      "  Downloading marshmallow_enum-1.5.1-py2.py3-none-any.whl (4.2 kB)\n",
      "Collecting typing-extensions>=3.6.5\n",
      "  Downloading typing_extensions-4.6.3-py3-none-any.whl (31 kB)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\programdata\\anaconda3\\lib\\site-packages (from requests<3,>=2->langchain) (3.3)\n",
      "Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\\programdata\\anaconda3\\lib\\site-packages (from requests<3,>=2->langchain) (1.26.9)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\programdata\\anaconda3\\lib\\site-packages (from requests<3,>=2->langchain) (2021.10.8)\n",
      "Requirement already satisfied: greenlet!=0.4.17 in c:\\programdata\\anaconda3\\lib\\site-packages (from SQLAlchemy<3,>=1.4->langchain) (1.1.1)\n",
      "Requirement already satisfied: packaging>=17.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from marshmallow<4.0.0,>=3.3.0->dataclasses-json<0.6.0,>=0.5.7->langchain) (21.3)\n",
      "Requirement already satisfied: mypy-extensions>=0.3.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from typing-inspect>=0.4.0->dataclasses-json<0.6.0,>=0.5.7->langchain) (0.4.3)\n",
      "Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in c:\\programdata\\anaconda3\\lib\\site-packages (from packaging>=17.0->marshmallow<4.0.0,>=3.3.0->dataclasses-json<0.6.0,>=0.5.7->langchain) (3.0.4)\n",
      "Installing collected packages: typing-extensions, tenacity, numexpr, typing-inspect, pydantic, marshmallow, openapi-schema-pydantic, marshmallow-enum, aiohttp, dataclasses-json, langchain\n",
      "Successfully installed aiohttp-3.8.4 dataclasses-json-0.5.7 langchain-0.0.190 marshmallow-3.19.0 marshmallow-enum-1.5.1 numexpr-2.8.4 openapi-schema-pydantic-1.2.4 pydantic-1.10.8 tenacity-8.2.2 typing-extensions-4.6.3 typing-inspect-0.9.0\n"
     ]
    }
   ],
   "source": [
    "pip install langchain"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "144af1d7",
   "metadata": {},
   "source": [
    "#### Open AI\n",
    "\n",
    "The OpenAI Python library provides convenient access to the OpenAI API from applications written in the Python language. It includes a pre-defined set of classes for API resources that initialize themselves dynamically from API responses which makes it compatible with a wide range of versions of the OpenAI API."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "19f72b5e",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Collecting openai\n",
      "  Downloading openai-0.27.7-py3-none-any.whl (71 kB)\n",
      "     ---------------------------------------- 72.0/72.0 kB 1.3 MB/s eta 0:00:00\n",
      "Requirement already satisfied: requests>=2.20 in c:\\programdata\\anaconda3\\lib\\site-packages (from openai) (2.27.1)\n",
      "Requirement already satisfied: tqdm in c:\\programdata\\anaconda3\\lib\\site-packages (from openai) (4.64.0)\n",
      "Requirement already satisfied: aiohttp in c:\\users\\saija\\appdata\\roaming\\python\\python39\\site-packages (from openai) (3.8.4)\n",
      "Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\\programdata\\anaconda3\\lib\\site-packages (from requests>=2.20->openai) (1.26.9)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\programdata\\anaconda3\\lib\\site-packages (from requests>=2.20->openai) (2021.10.8)\n",
      "Requirement already satisfied: charset-normalizer~=2.0.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from requests>=2.20->openai) (2.0.4)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\programdata\\anaconda3\\lib\\site-packages (from requests>=2.20->openai) (3.3)\n",
      "Requirement already satisfied: yarl<2.0,>=1.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from aiohttp->openai) (1.6.3)\n",
      "Requirement already satisfied: frozenlist>=1.1.1 in c:\\programdata\\anaconda3\\lib\\site-packages (from aiohttp->openai) (1.2.0)\n",
      "Requirement already satisfied: async-timeout<5.0,>=4.0.0a3 in c:\\programdata\\anaconda3\\lib\\site-packages (from aiohttp->openai) (4.0.1)\n",
      "Requirement already satisfied: attrs>=17.3.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from aiohttp->openai) (21.4.0)\n",
      "Requirement already satisfied: multidict<7.0,>=4.5 in c:\\programdata\\anaconda3\\lib\\site-packages (from aiohttp->openai) (5.1.0)\n",
      "Requirement already satisfied: aiosignal>=1.1.2 in c:\\programdata\\anaconda3\\lib\\site-packages (from aiohttp->openai) (1.2.0)\n",
      "Requirement already satisfied: colorama in c:\\programdata\\anaconda3\\lib\\site-packages (from tqdm->openai) (0.4.4)\n",
      "Requirement already satisfied: typing-extensions>=3.6.5 in c:\\users\\saija\\appdata\\roaming\\python\\python39\\site-packages (from async-timeout<5.0,>=4.0.0a3->aiohttp->openai) (4.6.3)\n",
      "Installing collected packages: openai\n",
      "Successfully installed openai-0.27.7\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "  WARNING: The script openai.exe is installed in 'C:\\Users\\saija\\AppData\\Roaming\\Python\\Python39\\Scripts' which is not on PATH.\n",
      "  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.\n",
      "\n",
      "[notice] A new release of pip available: 22.2.2 -> 23.1.2\n",
      "[notice] To update, run: python.exe -m pip install --upgrade pip\n"
     ]
    }
   ],
   "source": [
    "pip install openai"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "8751e5cd",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Requirement already satisfied: pip in c:\\users\\saija\\appdata\\roaming\\python\\python39\\site-packages (22.2.2)\n",
      "Collecting pip\n",
      "  Downloading pip-23.1.2-py3-none-any.whl (2.1 MB)\n",
      "     ---------------------------------------- 2.1/2.1 MB 7.8 MB/s eta 0:00:00\n",
      "Installing collected packages: pip\n",
      "  Attempting uninstall: pip\n",
      "    Found existing installation: pip 22.2.2\n",
      "    Uninstalling pip-22.2.2:\n",
      "      Successfully uninstalled pip-22.2.2\n",
      "Successfully installed pip-23.1.2\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "  WARNING: The scripts pip.exe, pip3.10.exe, pip3.9.exe and pip3.exe are installed in 'C:\\Users\\saija\\AppData\\Roaming\\Python\\Python39\\Scripts' which is not on PATH.\n",
      "  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.\n"
     ]
    }
   ],
   "source": [
    "pip install --upgrade pip"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "64cd8b94",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Collecting pypdf\n",
      "  Downloading pypdf-3.9.1-py3-none-any.whl (249 kB)\n",
      "     -------------------------------------- 249.3/249.3 kB 3.1 MB/s eta 0:00:00\n",
      "Requirement already satisfied: typing_extensions>=3.10.0.0 in c:\\users\\saija\\appdata\\roaming\\python\\python39\\site-packages (from pypdf) (4.6.3)\n",
      "Installing collected packages: pypdf\n",
      "Successfully installed pypdf-3.9.1\n"
     ]
    }
   ],
   "source": [
    "!pip install pypdf"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "684f3f50",
   "metadata": {},
   "source": [
    "### Faiss-cpu\n",
    "\n",
    "Faiss is a library for efficient similarity search and clustering of dense vectors. It contains algorithms that search in sets of vectors of any size, up to ones that possibly do not fit in RAM. It also contains supporting code for evaluation and parameter tuning. Faiss is written in C++ with complete wrappers for Python/numpy. It is developed by Facebook AI Research."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "17e252af",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Collecting faiss-cpu\n",
      "  Downloading faiss_cpu-1.7.4-cp39-cp39-win_amd64.whl (10.8 MB)\n",
      "     --------------------------------------- 10.8/10.8 MB 10.7 MB/s eta 0:00:00\n",
      "Installing collected packages: faiss-cpu\n",
      "Successfully installed faiss-cpu-1.7.4\n"
     ]
    }
   ],
   "source": [
    "!pip install faiss-cpu"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "f106681f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Collecting tiktoken\n",
      "  Downloading tiktoken-0.4.0-cp39-cp39-win_amd64.whl (635 kB)\n",
      "     -------------------------------------- 635.6/635.6 kB 5.0 MB/s eta 0:00:00\n",
      "Requirement already satisfied: regex>=2022.1.18 in c:\\programdata\\anaconda3\\lib\\site-packages (from tiktoken) (2022.3.15)\n",
      "Requirement already satisfied: requests>=2.26.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from tiktoken) (2.27.1)\n",
      "Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\\programdata\\anaconda3\\lib\\site-packages (from requests>=2.26.0->tiktoken) (1.26.9)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\programdata\\anaconda3\\lib\\site-packages (from requests>=2.26.0->tiktoken) (2021.10.8)\n",
      "Requirement already satisfied: charset-normalizer~=2.0.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from requests>=2.26.0->tiktoken) (2.0.4)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\programdata\\anaconda3\\lib\\site-packages (from requests>=2.26.0->tiktoken) (3.3)\n",
      "Installing collected packages: tiktoken\n",
      "Successfully installed tiktoken-0.4.0\n"
     ]
    }
   ],
   "source": [
    "!pip install tiktoken"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "95267a1f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Paste your OpenAI API key here and hit enter:········\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "from getpass import getpass\n",
    "\n",
    "os.environ[\"OPENAI_API_KEY\"] = getpass(\"Paste your OpenAI API key here and hit enter:\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "d3b7df21",
   "metadata": {},
   "outputs": [],
   "source": [
    "from langchain.llms import OpenAI"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "5a1ef147",
   "metadata": {},
   "outputs": [],
   "source": [
    "from langchain.document_loaders import PyPDFLoader\n",
    "\n",
    "loader = PyPDFLoader(\"cucm_b_troubleshooting-guide-1251-extracted (1).pdf\")\n",
    "pages = loader.load()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "845c6439",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Document(page_content='CHAPTER 1\\nTroubleshooting Overview\\nThis section provides the necessary background information and available resources to troubleshoot theCisco\\nUnified Communications Manager .\\n•Cisco Unified Serviceability, on page 1\\n•Cisco Unified Communications Operating System Administration, on page 2\\n•General Model of Problem Solving, on page 2\\n•Network Failure Preparation, on page 3\\n•Where to Find More Information, on page 3\\nCisco Unified Serviceability\\nCisco Unified Serviceability, a web-based troubleshooting tool for Unified Communications Manager, provides\\nthe following functionality to assist administrators troubleshoot system problems:\\n• Saves Unified Communications Manager services alarms and events for troubleshooting and provi des\\nalarm message definitions.\\n•Saves Unified Communications Manager services trace information to various log files for troubleshooting .\\nAdministrators can configure, collect, and view trace information.\\n• Monitors real-time behavior of the components in a Unified Communications Manager cluster through\\nthe real-time monitoring tool (RTMT).\\n•Generates reports for Quality of Service, traffic, and billing informati on through Unified Communications\\nManager CDR Analysis and Reporting (CAR).\\n• Provides feature services that you can activate, deactivate, and view through the Servi ce Activation\\nwindow.\\n• Provides an interface for starting and stopping feature and network services.\\n• Archives reports that are associated with Cisco Unified Serviceability tools.\\n• Allows Unified Communications Manager to work as a managed device for SNMP remote ma nagement\\nand troubleshooting.\\n• Monitors the disk usage of the log partition on a server (or all servers in the cluster).\\nTroubleshooting Guide for Cisco Unified Communications Manager, Release 12.5(1)\\n1', metadata={'source': 'cucm_b_troubleshooting-guide-1251-extracted (1).pdf', 'page': 0})"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pages[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "95c76df1",
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "'list' object has no attribute 'split'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "Input \u001b[1;32mIn [15]\u001b[0m, in \u001b[0;36m<cell line: 3>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mlangchain\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mtext_splitter\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m CharacterTextSplitter\n\u001b[0;32m      2\u001b[0m text_splitter \u001b[38;5;241m=\u001b[39m CharacterTextSplitter\u001b[38;5;241m.\u001b[39mfrom_tiktoken_encoder(chunk_size\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m1000\u001b[39m, chunk_overlap\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m0\u001b[39m)\n\u001b[1;32m----> 3\u001b[0m texts \u001b[38;5;241m=\u001b[39m \u001b[43mtext_splitter\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43msplit_text\u001b[49m\u001b[43m(\u001b[49m\u001b[43mpages\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[1;32m~\\AppData\\Roaming\\Python\\Python39\\site-packages\\langchain\\text_splitter.py:243\u001b[0m, in \u001b[0;36mCharacterTextSplitter.split_text\u001b[1;34m(self, text)\u001b[0m\n\u001b[0;32m    241\u001b[0m \u001b[38;5;124;03m\"\"\"Split incoming text and return chunks.\"\"\"\u001b[39;00m\n\u001b[0;32m    242\u001b[0m \u001b[38;5;66;03m# First we naively split the large input into a bunch of smaller ones.\u001b[39;00m\n\u001b[1;32m--> 243\u001b[0m splits \u001b[38;5;241m=\u001b[39m \u001b[43m_split_text\u001b[49m\u001b[43m(\u001b[49m\u001b[43mtext\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_separator\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_keep_separator\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m    244\u001b[0m _separator \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m\"\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_keep_separator \u001b[38;5;28;01melse\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_separator\n\u001b[0;32m    245\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_merge_splits(splits, _separator)\n",
      "File \u001b[1;32m~\\AppData\\Roaming\\Python\\Python39\\site-packages\\langchain\\text_splitter.py:44\u001b[0m, in \u001b[0;36m_split_text\u001b[1;34m(text, separator, keep_separator)\u001b[0m\n\u001b[0;32m     42\u001b[0m         splits \u001b[38;5;241m=\u001b[39m [_splits[\u001b[38;5;241m0\u001b[39m]] \u001b[38;5;241m+\u001b[39m splits\n\u001b[0;32m     43\u001b[0m     \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[1;32m---> 44\u001b[0m         splits \u001b[38;5;241m=\u001b[39m \u001b[43mtext\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43msplit\u001b[49m(separator)\n\u001b[0;32m     45\u001b[0m \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[0;32m     46\u001b[0m     splits \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mlist\u001b[39m(text)\n",
      "\u001b[1;31mAttributeError\u001b[0m: 'list' object has no attribute 'split'"
     ]
    }
   ],
   "source": [
    "from langchain.text_splitter import CharacterTextSplitter\n",
    "text_splitter = CharacterTextSplitter.from_tiktoken_encoder(chunk_size=1000, chunk_overlap=0)\n",
    "texts = text_splitter.split_text(pages)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c7f32909",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
